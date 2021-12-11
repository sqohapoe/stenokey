class CombokeyToggleManager():
    def __init__(self, sm, lm, vm=None):
        self.sm = sm
        self.lm = lm
        self.vm = vm
        self.stenokey_on = False
        self.liukey_on = False
        self.vimium_on = False
                
    def reload(self):
        self.sm.load()
        self.lm.load()
        self.vm.load()
        
    def set_sensitivity(self, sensitivity_number):
        assert 0<= sensitivity_number <= 100
        self.sm.THRESHOLD_OVERLAP_2 = (100-sensitivity_number)/100
        
    def toggle_steno(self):
        self.stenokey_on = not self.stenokey_on
        if self.stenokey_on:
            self.sm.hook()
        else:
            self.sm.unhook()
            
    def toggle_liu(self):
        self.liukey_on = not self.liukey_on
        if self.liukey_on:
            self.lm.hook()
        else:
            self.lm.unhook()
            
    def toggle_vimium(self):
        self.vimium_on = not self.vimium_on
        if self.vimium_on:
            self.vm.hook()
        else:
            self.vm.unhook()
            
    def deactivate(self):
        self.stenokey_was_on = self.stenokey_on
        self.liukey_was_on = self.liukey_on
        self.vimium_was_on = self.vimium_on
        if self.stenokey_was_on:
            self.toggle_steno()
        if self.liukey_was_on:
            self.toggle_liu()
        if self.vimium_was_on:
            self.toggle_vimium()
    
    def reactivate(self):
        if self.stenokey_was_on:
            self.toggle_steno()
        if self.liukey_was_on:
            self.toggle_liu()
        if self.vimium_was_on:
            self.toggle_vimium()
        