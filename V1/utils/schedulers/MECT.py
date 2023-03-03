"""
Author: Ali Mokhtari (ali.mokhtaary@gmail.com)
Created on Nov., 15, 2021


"""

from utils.base_task import TaskStatus
from utils.base_scheduler import BaseScheduler
import utils.config as config
from utils.event import Event, EventTypes
import time
import numpy as np


class MECT(BaseScheduler):
    

    def __init__(self, total_no_of_tasks):
        super().__init__()
        self.name = 'MECT'
        self.total_no_of_tasks = total_no_of_tasks
        self.sleep_time = 0.1
        

    def choose(self, index=0):
        task = self.batch_queue.get(index)     
        self.unmapped_task.append(task)
        if config.gui==1:
            self.decision.emit({'type':'choose',
                                'time':config.time.gct(),
                                'where':'simulator: choose',
                                'data': {'task':task,
                                        'bq_indx': index,
                                        },                                
                                        })
            time.sleep(self.sleep_time)
        
        if config.settings['verbosity']:
            s =f'\n{task.id} selected --> BQ = '
            bq = [t.id for t in self.batch_queue.list]
            s += f'{bq}'
            s += f'\nexecutime: {task.execution_time}'
            s += f'\testimeated_time{task.estimated_time}'

            config.log.write(s)
        
        return task
    
    
    
    def map(self, machine):
        task = self.unmapped_task.pop()
        machine.admit(task)        
        task.assigned_machine = machine
        self.stats['mapped'].append(task)
        if config.gui==1:
                self.decision.emit({'type':'map',
                                'time':config.time.gct(),
                                'where':'scheduler: map',
                                'data': {'task':task,
                                         'assigned_machine':machine,                                    
                                        },
                                        })
                time.sleep(self.sleep_time)
        
    

    def schedule(self):
        self.gui_machine_log = []
        
        if config.settings['verbosity']:
            s = f'\n Current State @{config.time.gct()}'
            s = '\nBQ = '
            bq = [t.id for t in self.batch_queue.list]
            s += f'{bq}'
            s += '\n\nMACHINES ==>>>'
            for m in config.machines:
                s += f'\n\tMachine {m.type.name} :'
                if m.running_task:
                    r = [m.running_task[0].id]
                else:
                    r = []
                mq = [t.id for t in m.queue.list]
                r.append(mq)
                s +=f'\t{r}'
            config.log.write(s)

        
        if not self.batch_queue.empty():
            task = self.choose()
            
            pcts = [[machine.provisional_map(task), machine.id] for machine in config.machines]           
            min_pct = min(pcts, key=lambda x:x[0])[0]            
            pcts = np.array(pcts)
            ties = pcts[pcts[:,0] == min_pct]
            np.random.seed(task.id)
            assigned_machine_idx = int(np.random.choice(ties[:,1]))            
            assigned_machine = config.machines[assigned_machine_idx]

            self.map(assigned_machine)
            s = f"\ntask:{task.id}  assigned to:{assigned_machine.type.name}  delta:{task.deadline} min_pct:{min_pct}"
            config.log.write(s)     
                       
            return assigned_machine
        
    #####
    