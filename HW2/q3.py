
class List(list):

    def get(self, *args):
        temp = super().__getitem__(args[0][0])
        for index in args[0][1:]:
            temp = temp[index]
        return temp

    def __getitem__(self, *args):
        if isinstance(*args,int):
            return self.get(args)
        return self.get(*args)

    def __setitem__(self, args, value):
        print(args)
        if isinstance(args,int):
            super().__setitem__(args, value)
        else:
            temp = super().__getitem__(args[0])
            for index in args[1:-1]:
                temp = temp[index]
            temp[args[-1]] = value


if __name__ == '__main__':

    mylist = List([13, 14, 15, 155])
    mylist.append(([1, ([333]), 1, 1]))
    print(mylist)
    print(mylist[4])
    mylist[4] = 0
    print(mylist[4])
    print(mylist)

