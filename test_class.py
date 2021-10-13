class test_obj:

    def __init__(self, input_dic = ["not empty"]):
        self.dic = input_dic


if __name__ == "__main__":

    test1 = test_obj()
    test2 = test_obj()

    test1.dic.append("test1_obj")
    test2.dic.append("test2_obj")
    print(test1.dic)