#!/usr/bin/env python3

import sys
import re

if __name__ == '__main__':
    in_table = False
    t = []
    t_done = True

    for line in sys.stdin:
        line = line.rstrip()
        if re.search('\\\\begin{.*longtable.*', line):
            in_table = True
            t_done = False
        elif re.search('\\\\end{.*longtable.*', line):
            in_table = False
            t.append(line)

        if in_table:
            t.append(line)
        elif t_done and not in_table:
            print(line)
        elif not t_done:
            #t[0] = t[0].replace('r', 'S')
            table_format = re.sub('longtable', 'tabular', t[0]).replace('[c]', '[htbp]')
            t[0] = '\\begin{table}\n\\centering'
            t[-1] = '\\end{tabular}\n\\end{table}'

            caption_index = [i for i, item in enumerate(t) if re.search('\\\\caption', item)]
            if len(caption_index) > 0:
                caption = t.pop(caption_index[0])
                t.insert(1, caption)

            rules = [i for i, item in enumerate(t) if re.search('(\\\\hline|\\\\toprule|\\\\midrule|\\\\bottomrule)', item)]
            aligns = [i for i, item in enumerate(t) if re.search('\\\\noalign{\\\\medskip}', item)]

            for i in aligns:
                t[i] = '\\\\'

            if len(rules) > 0:
                top_rule = rules.pop(0)
                t[top_rule] = '\\toprule' # \\endhead
                if len(rules) > 0:
                    bottom_rule = rules.pop()
                    t.pop(bottom_rule)
                    t.insert(-1, '\\bottomrule')
                    if t[-3] == '\\\\' and t[-4] == '\\\\':
                        t.pop(-3)
                for i in rules:
                    t[i] = '\\midrule'

            totals = [i for i, item in enumerate(t) if re.search('TOTAL', item)]
            for i in totals:
                if t[i-1] == '\\\\':
                    t[i-1] += '\\midrule'
                elif t[i-2] == '\\\\':
                    t[i-2] += '\\midrule'

            top_rule_pos = [i for i, item in enumerate(t) if re.search('\\\\toprule', item)][0]
            t.insert(top_rule_pos, table_format)
            # FIXME odd/even page margin tuning with macro and \begin{adjustwidth}{-1in}{-1in}
            #print('\\begin{adjustwidth}{\\lmargin}{\\rmargin}')
            #print('\\expandtablemargins{\n\\begin{center}')
            print('\n'.join(t)) # .replace('\\\\', '\\\\*')
            #print('\\end{center}\n}')
            t = []
            t_done = True

        else:
            raise(Exception('DEBUG:' + line))
