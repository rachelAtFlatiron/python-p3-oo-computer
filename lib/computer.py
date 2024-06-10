import ipdb 
class Computer:
    
    #class attribute
    all_brands = []
    all_models = []
    all = []

    def __init__(self, brand, model, storage_free):
        # _ represents the attribute is meant to be private
        # directly updating the private attribute will circumvent the property setter
        self.brand = brand 
        self._model = model 
        self._memory_GB = 8
        self._storage_free = storage_free
        Computer.all_brands.append(brand)
        Computer.all_models.append(model)
        Computer.all.append(self)

    @classmethod 
    def brands(cls):
        return list(set(Computer.all_brands))
    
    @classmethod 
    def models(cls):
        return list(set(Computer.all_models))
    

    
    # [c1, c2, c3, c4]
    # biggest (start as the first instance) - responsible for storing instance with largest memory that we have SEEN SO FAR
    # cur (start at 2nd instance) - stores current instance that we are comparing to
    @classmethod 
    def largest_memory(cls):
        return max(Computer.all, key=lambda cur: cur.storage_free)

        biggest = Computer.all[0]
        #iterate over all computer instances
        for i in range(1, len(Computer.all)):
            cur = Computer.all[i]
            if(cur.storage_free > biggest.storage_free):
                biggest = cur 
        return biggest
    
    # RAM is a dictionary 
    def upgrade_memory(self, RAM):
        self.memory_GB = self._memory_GB + RAM['size']

    def is_disk_full(self, file_size):
        return True if file_size <= self.storage_free else False
    
    def save_file(self, file):
        if(self.is_disk_full(file['size'])):
            self.storage_free = self.storage_free - file['size']
            return f"{file['name']} has been saved!"
        else:
            return f"There is not enough space on disk to save {file['name']}."
        
    def delete_file(self, file):
        #check if size is valid (not neg, doesn't leave with more mem)
        self.storage_free = self.storage_free + file['size']
        return f"{file['name']} has been deleted!"
    
    
    def specs(self):
        return f'Current memory: {self.memory_GB} and current storage: {self.storage_free}'
    
    @property 
    def brand(self):
        return self._brand
    
    @brand.setter 
    def brand(self, new_brand):
        if(not hasattr(self, 'brand') and new_brand != ''):
            self._brand = new_brand
        else:
            print('no')

    @property 
    def model(self):
        return self._model
    
    @property 
    def memory_GB(self):
        return self._memory_GB
    
    @memory_GB.setter 
    def memory_GB(self, new_mem):
        if(0 <= new_mem <= 32):
            self._memory_GB = new_mem 
        else:
            print('no')

    @property 
    def storage_free(self):
        return self._storage_free
    
    @storage_free.setter 
    def storage_free(self, new_storage_free):
        if(0 <= new_storage_free <= 1000):
            self._storage_free = new_storage_free
        else:
            raise Exception

    def __repr__(self):
        return f'<Computer memory={self.memory_GB} storage={self.storage_free} brand={self.brand} model={self.model} />' 
    


if __name__ == "__main__":
    f1 = {'name': 'f1', 'size': 100}
    f2 = {'name': 'f2', 'size': 200}
    c1 = Computer('test', 'test', 500)
    c2 = Computer('two', 'two', 100)
    c3 = Computer('two', 'two', 1000)
    c4 = Computer('two', 'two', 200)
    c5 = Computer('two', 'two', 500)
    ipdb.set_trace()


'''

document.addEventListener('click', (c) => { return c.storage_free })
max([], key=lambda c: c.storage_free)
'''