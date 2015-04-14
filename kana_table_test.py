#!/usr/bin/env python3
# coding: utf-8

romaji = []
hiragana = []
katakana = []

def num_permuts(N):
    """Permutation of 0 -- 46
    """
    from random import shuffle as shf
    from random import seed
    seed()
    a = [i for i in range(N)]
    shf(a)
    return a[:]

def main(ts):
    import time

    # -------------------- read in kana data --------------------
    with open("share/kana_list.dat", 'r') as fin:
        for lines in fin:
            words = lines.split()
            if lines.startswith('#') or len(words) <= 1:
                continue
            if not words[1].isdigit():
                continue
            roma, hira, kata = words[3], words[5], words[7]
            romaji.append(roma)
            hiragana.append(hira)
            katakana.append(kata)

    # -------------------- test settings --------------------
    if ts == 1:
        nums = num_permuts(46)
        l_test = romaji
    elif ts == 2:
        nums = num_permuts(46)
        l_test = katakana
    elif ts == 3:
        nums = num_permuts(46)
        l_test = hiragana
    elif ts == 4:
        nums = num_permuts(46 * 3)
        l_test = romaji + hiragana + katakana
    else:
        print('    Wrong testing style!')
        exit()

    # Begin testing, log time spent on memory test -----------------------------
    t0 = time.time()
    t1 = t0
    t_log = {}                  # time log
    for i in nums[:10]:
        key_in = input(" " + l_test[i] + "\t")
        t2 = time.time()
        dt = t2 - t1
        t1 = t2
        j = i % 46
        if key_in == 'x':
            print(" \t", romaji[j], "\t", hiragana[j], "\t", katakana[j])
            dt += 2
        t_log[j] = round(dt, 2)

    t_final = time.time()
    s_t_out = time.ctime()

    s = s_t_out.split()
    out_filename = 'data/kana_test_result' + '_' + s[1] + '_' + s[2] + '_' + s[4] + '_' + s[3][:5]
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
        print(num, "\t", romaji[num], "  \t", hiragana[num], " \t", katakana[num], " \t", t, "s")
        fout.write(romaji[num].rjust(4) + ' \t')
        fout.write(str(hiragana[num]).ljust(4) + ' \t')
        fout.write(str(katakana[num]).ljust(4) + ' \t' + str(t).rjust(6) + ' s\n')
    print(" ============================================================")
    fout.write(" ============================================================\n")


if __name__ == '__main__':
    hint_str = ''' ========================
    日语假名记忆测试：
    请选择测试类型：
    1. 看罗马字回忆假名
    2. 看片假名回忆读音
    3. 看平假名回忆读音
    4. 混乱回忆
    ...
    '''
    try:
        test_style = int(input(hint_str))
    except:
        print('  Please choose from the list! ')
        exit()
    while test_style < 1 or test_style > 4:
        test_style = int(input('    Please input an integer between (1..4) > '))
    print("  ~~~~~~~~~~~~~~~~~~~~  ")
    main(test_style)
