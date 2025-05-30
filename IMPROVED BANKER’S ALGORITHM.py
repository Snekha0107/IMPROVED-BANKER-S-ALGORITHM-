import tkinter as tk 
from tkinter import messagebox 
 
class BankerAlgorithmGUI: 
    def __init__(self, root): 
        self.root = root 
        self.root.title("Banker's Algorithm") 
         
        self.max_label = tk.Label(root, text="Maximum Resources:") 
        self.max_label.pack() 
         
        self.max_entries = [] 
        self.allocation_entries = [] 
         
        self.num_processes = 0 
        self.num_resources = 0 
         
        self.add_process_button = tk.Button(root, text="Add Process", 
command=self.add_process) 
        self.add_process_button.pack() 
         
        self.run_button = tk.Button(root, text="Run Banker's Algorithm", 
command=self.run_algorithm) 
        self.run_button.pack() 
         
    def add_process(self): 
        if self.num_processes == 0: 
            self.num_resources = len(self.max_entries) + 1 
         
        process_frame = tk.Frame(root) 
        process_frame.pack() 
        
        max_resources_label = tk.Label(process_frame, text="Process {}: Maximum 
Resources:".format(self.num_processes)) 
        max_resources_label.pack(side=tk.LEFT) 
         
        allocation_resources_label = tk.Label(process_frame, text="Allocation 
Resources:") 
        allocation_resources_label.pack(side=tk.LEFT) 
         
        max_entries = [] 
        allocation_entries = [] 
         
        for i in range(self.num_resources): 
            max_entry = tk.Entry(process_frame, width=5) 
            max_entry.pack(side=tk.LEFT) 
            max_entries.append(max_entry) 
             
            allocation_entry = tk.Entry(process_frame, width=5) 
            allocation_entry.pack(side=tk.LEFT) 
            allocation_entries.append(allocation_entry) 
         
        self.max_entries.append(max_entries) 
        self.allocation_entries.append(allocation_entries) 
        self.num_processes += 1 
         
    def run_algorithm(self): 
        max_resources = [] 
        allocation_resources = [] 
 
        for i in range(self.num_processes): 
            max_entries = self.max_entries[i] 
            allocation_entries = self.allocation_entries[i] 
 
            max_resources.append([int(val) for entry in max_entries for val in 
entry.get().split() if val.strip()]) 
 
            allocation_resources.append([int(val) for entry in allocation_entries for val 
in entry.get().split() if val.strip()]) 
 
        available_resources = [int(val) for entry in self.allocation_entries[0] for val in 
entry.get().split() if val.strip()] 
 
        print("Max Resources:", max_resources) 
        print("Allocation Resources:", allocation_resources) 
        print("Available Resources:", available_resources) 
 
        result = self.bankers_algorithm(max_resources, allocation_resources, 
available_resources) 
 
        print("Finish Status:", result) 
 
        if result: 
            messagebox.showinfo("Banker's Algorithm", "The system is in a safe 
state.") 
        else: 
            messagebox.showinfo("Banker's Algorithm", "The system is in an unsafe 
state.") 
 
         
    def bankers_algorithm(self, max_resources, allocation_resources, 
available_resources): 
        num_processes = len(max_resources) 
        num_resources = len(available_resources) 
 
        work = available_resources.copy() 
        finish = [False] * num_processes 
 
        need = [] 
        for i in range(num_processes): 
            need.append([max_resources[i][j] - allocation_resources[i][j] for j in 
range(num_resources)]) 
 
        count = 0 
        while count < num_processes: 
            found = False 
            for i in range(num_processes): 
                if not finish[i]: 
                    if all(need[i][j] <= work[j] for j in range(num_resources)): 
                        work = [work[j] + allocation_resources[i][j] for j in 
range(num_resources)] 
                        finish[i] = True 
                        found = True 
                        count += 1 
 
            if not found: 
                break 
 
        return all(finish) 
if __name__ == "__main__": 
    root = tk.Tk() 
    app = BankerAlgorithmGUI(root) 
    root.mainloop() 