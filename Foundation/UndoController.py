class UndoController:
    def __init__(self):
        self.actions = []
        self.cur_undo = -1
        self.in_action = False
        self.macro_action = None
        self.temp = None
        self.count = 0

    # 重新执行操作
    def redo(self):
        self.in_action = True
        # print('ActionManager.do()')
        if not self.redone():
            cur_do = self.__cur_do
            self.__set_cur_do(self.__cur_do + 1)
            self.actions[cur_do].do()
        self.in_action = False
        # print("self.cur_do=", self.cur_do, ",self.cur_undo=", self.cur_undo)

    # false：redo操作结束
    def redone(self):
        ret = (self.__cur_do < 0) or (self.__cur_do >= len(self.actions))
        # print('ActionManager.done=', ret)
        return ret

    # undo操作
    def undo(self):
        self.in_action = True
        # print('ActionManager.undo()')
        if not self.undone():
            cur_undo = self.cur_undo
            self.cur_undo = self.cur_undo - 1
            self.actions[cur_undo].undo()
        self.in_action = False
        # print("self.cur_do=", self.cur_do, ",self.cur_undo=", self.cur_undo)

    # ture: undo操作结束
    def undone(self):
        ret = (self.cur_undo < 0) or (self.cur_undo >= len(self.actions))
        # print('ActionManager.undone=', ret)
        return ret

   # 添加Action
    def _add_action(self, action):
        new_current = self.cur_undo + 1
        if new_current < len(self.actions):
            while len(self.actions) > new_current:
                self.actions.pop()
        self.actions.append(action)
        self.cur_undo = new_current

    # 取得当前执行Action索引
    @property
    def __cur_do(self):
        return self.cur_undo + 1

    # 执行当前执行Action索引
    def __set_cur_do(self, do):
        self.cur_undo = do - 1

    def __print(self):
        if len(self.actions)!= self.count:
            print(self)
            for index in range(0, len(self.actions)):
                if index == self.__cur_do:
                    print(type(self.actions[index]), 'cur_do')
                elif index == self.cur_undo:
                    print(type(self.actions[index]), 'cur_undo')
                else:
                    print(type(self.actions[index]))
            self.count = len(self.actions)


