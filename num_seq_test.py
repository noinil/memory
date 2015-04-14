#!/usr/bin/env python3

def num_sequence(n):
    """Generate a sequence of random numbers
    n: length of the generated sequence
    """
    import random
    random.seed()
    la = ""
    for i in range(n):
        la = la + str(random.randrange(10))
    return la

def main():
    import time
    import os

    # Generate permutation for test --------------------------------------------
    hint_str = '''Please input the length of the number sequence:
    (default: 20):
    '''
    try:
        len_num_seq = int(input(hint_str))
    except:
        len_num_seq = 20
    nums = num_sequence(len_num_seq)

    # Begin testing, log time spent on memory test -----------------------------
    t0 = time.time()
    t1 = t0
    key_in = input(" " + nums + "\t")
    os.system("clear")
    t2 = time.time()
    dt1 = t2 - t1
    recall_seq = input(" recall > ")
    t3 = time.time()
    dt2 = t3 - t2

    s_t_out = time.ctime()

    s = s_t_out.split()
    out_filename = 'data/num_seq_memo_' + s[1] + '_' + s[2] + '_' + s[4] + '_' + s[3][:5]
    fout = open(out_filename, 'w')

    print(" ============================================================")
    print(" You spent ", round(dt1 + dt2), " seconds totally. ")
    print(" ------------------------------------------------------------")

    fout.write(" ============================================================\n")
    fout.write(" You spent " + str(round(dt1 + dt2)) + " seconds totally. \n")
    fout.write(" ------------------------------------------------------------\n")

    # Analyze the results ------------------------------------------------------
    print(" The correct answer is:", nums)
    print(' Learning time: ' + str(round(dt1, 2)).rjust(6) + ' s')
    print(' Recall time:   ' + str(round(dt2, 2)).rjust(6) + ' s')
    fout.write(' Length of list:' + str(len(nums)).rjust(6) + '\n')
    fout.write(' Learning time: ' + str(round(dt1, 2)).rjust(6) + ' s\n')
    fout.write(' Recall time:   ' + str(round(dt2, 2)).rjust(6) + ' s\n')
    if recall_seq == nums:
        print(" You succeeded!  Congratulations!")
        fout.write(' WIN!  Your answer is correct!  Congratulations!\n')
    else:
        print(" Your answer is incorrect!  You are stupid.")
        fout.write(" LOSE!  Your answer is incorrect!  You are stupid.")
    print(" ============================================================")
    fout.write(" ============================================================\n")

if __name__ == '__main__':
    main()
