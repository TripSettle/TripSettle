
class TripExpendSettle:
    def __init__(self,expend):
        self.expend = expend
        self.expend_flag = {'person1':False,'person2':False,'person3':False,'person4':False}
        self.expend_res={"person1":[],"person2":[],"person3":[],"person4":[]}
        print(self.expend)
    def findmin(self,expend):
        min_key=""
        min_val=0
        for key,value in expend.items():
            if min_val > value:
                if value < 0:
                    min_val=value
                    min_key=key
        return min_key

    def findmax(self,expend):
        max_key=""
        max_val=0
        for key,value in expend.items():
            if max_val < value:
                if value > 0:
                    max_val=value
                    max_key=key
        return max_key
    def SettleUp(self):
        while False in self.expend_flag.values():
            min_key = self.findmin(self.expend)
            max_key = self.findmax(self.expend)
            tally = self.expend[max_key]+self.expend[min_key]

            if tally < 0:
                self.expend_res[max_key].append(f"{max_key} will receive amount {self.expend[max_key]} from {min_key}")
                self.expend_res[min_key].append(f"{min_key} will give amount {self.expend[max_key]} to {max_key}")
                self.expend_flag[max_key] = True
                self.expend[max_key] =0
                self.expend[min_key] = tally
            elif tally > 0:
                self.expend_res[max_key].append(f"{max_key} will receive amount {self.expend[min_key]*-1} from {min_key}")
                self.expend_res[min_key].append(f"{min_key} will give amount {self.expend[min_key]*-1} to {max_key}")
                self.expend_flag[min_key] = True
                self.expend[min_key] =0
                self.expend[max_key] = tally
            else:
                self.expend_res[max_key].append(f"{max_key} will receive amount {self.expend[min_key]*-1} from {min_key}")
                self.expend_res[min_key].append(f"{min_key} will give amount {self.expend[min_key]*-1} to {max_key}")
                self.expend_flag[min_key] = True
                self.expend_flag[max_key] = True
                self.expend[min_key] =0
                self.expend[max_key] = 0
        return self.expend_res

