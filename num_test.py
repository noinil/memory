#!/usr/bin/env python3

def num_permuts():
    """Permutation of 01 -- 100
    """
    from random import shuffle as shf
    a = [i + 1 for i in range(100)]
    shf(a)
    return a[:]

def main():
    import time

    # read in abracadabra ------------------------------------------------------
    abracadabra = {}            # Store number : association pairs -------------
    with open('share/num_list.dat', 'r') as fin_data:
        for lines in fin_data:
            words = lines.split()
            num, word = float(words[0]), words[1]
            abracadabra[num] = word

    # Generate permutation for test --------------------------------------------
    nums = num_permuts()

    # Begin testing, log time spent on memory test -----------------------------
    t0 = time.time()
    t1 = t0
    t_log = {}                  # time log
    for i in nums:
        key_in = input(" " + str(i) + "\t")
        t2 = time.time()
        dt = t2 - t1
        t1 = t2
        if key_in == 'x':
            print(" \t", abracadabra[i])
            dt += 2
        t_log[i] = round(dt, 2)

    t_final = time.time()
    s_t_out = time.ctime()

    s = s_t_out.split()
    out_filename = 'data/num_test_result' + '_' + s[1] + '_' + s[2] + '_' + s[4] + '_' + s[3][:5]
    fout = open(out_filename, 'w')

    print(" ============================================================")
    print(" You spent ", round(t_final - t0), " seconds. ")
    print(" ------------------------------------------------------------")

    fout.write(" ============================================================\n")
    fout.write(" You spent " + str(round(t_final - t0)) + " seconds. \n")
    fout.write(" ------------------------------------------------------------\n")

    # Analyze the results ------------------------------------------------------
    t_log_sorted = sorted(t_log.items(), key=lambda x:x[1], reverse = True)
    for i in t_log_sorted:
        num, t = i[0], i[1]
        print(num, "\t", abracadabra[num], "     \t", t, "s")
        fout.write(str(num).rjust(4) + ' \t')
        fout.write(str(abracadabra[num]).ljust(5) + '    \t' + str(t) + ' s\n')
    print(" ============================================================")
    fout.write(" ============================================================")

if __name__ == '__main__':
    main()
