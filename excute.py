# -*- coding: utf-8 -*-
import sys
from preprocess import Channel
from workflow.cf_workflow import run as user_cf
from workflow.lfm_workflow import run as lfm
from workflow.prank_workflow import run as prank
import traceback

def delete_substr_method2(in_str, in_substr):
    start_loc = in_str.find(in_substr)
    len_substr = len(in_substr)
    res_str = in_str[:start_loc] + in_str[start_loc + len_substr:]
    return res_str

def manage():
    arg = sys.argv[1]
    if arg == 'preprocess':
        Channel().process()
    elif arg == 'excute':
        target = int(sys.argv[2])  # 这里用运行参数代表用户id赋值给target
        result1 = user_cf()
        result2 = lfm(target)
        result3 = prank(target)#三个result的输出格式为[[str，浮点数],[str，浮点数]......]
        result1 = list(result1)
        result2 = list(result2)
        result3 = list(result3)
        result = []
        count = 0

        for i in result2:
            for j in result3:
                for k in result1:
                    i = list(i)
                    j = list(j)
                    k = list(k)
                    if i[0] == delete_substr_method2(j[0],"item_") == k[0]:
                        result.append(i[0])
                        i[1] = 100
                        j[1] = 100
                        k[1] = 100
                    elif i[0] == delete_substr_method2(j[0],"item_") :
                        result.append(i[0])
                        i[1] = 100
                        j[1] = 100
                    elif k[0] == i[0]:
                        result.append(i[0])
                        k[1] = 100
                        i[1] = 100
                    elif k[0] == delete_substr_method2(j[0],"item_") :
                        result.append(k[0])
                        k[1] = 100
                        j[1] = 100
                    else:
                        for i in result2:
                            for j in result3:
                                for k in result1:
                                    if i[1]!=100:
                                        result.append(i[0])
                                    if j[1]!=100:
                                        result.append(delete_substr_method2(j[0],"item_"))
                                    if k[1] != 100:
                                        result.append(k[0])

        with open("recommand_result_"+sys.argv[2]+".txt",'w', encoding='utf-8') as f:
            for ok in result:
                if count < 10:
                    print(ok)
                    f.write(str(ok)+"\n")
                    count = count+1
    else:
        print('Args must in ["preprocess", "excute"].')
    sys.exit()


if __name__ == '__main__':
    target = 5
    manage()
