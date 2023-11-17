# f'testing/latin/text/edit_text/vergil/aen{i}.txt'
# f'testing/latin/text/edit_text/caesar/gall{i}.txt'
# f'testing/latin/text/edit_text/ovid/ovid.amor{i}.txt'
# f'testing/latin/text/edit_text/ovid/ovid.artis{i}.txt'
# f'testing/latin/text/edit_text/ovid/ovid.tristia{i}.txt'

remove = ['ab', 'ac', 'ad', 'adhic', 'aliqui', 'aliquis', 'an', 'ante', 'apud', 
          'at', 'atque', 'aut', 'autem', 'cum', 'cur', 'de', 'deinde', 'dum', 
          'ego', 'enim', 'ergo', 'es', 'est', 'et', 'etiam', 'etsi', 'ex', 'fio',
            'haud', 'hic', 'iam', 'idem', 'igitur', 'ille', 'in', 'infra', 'inter',
              'interim', 'ipse', 'is', 'ita', 'magis', 'modo', 'mox', 'nam', 'ne', 'nec', 
              'necque', 'neque', 'nisi', 'non', 'nos', 'o', 'ob', 'per', 'possum', 'post', 
              'qui', 'quia', 'quicumque', 'quidem', 'quilibet', 'quis', 
              'quisnam', 'quisquam', 'quisque', 'quisquis', 'quo', 'quoniam', 
              'sed', 'si', 'sic', 'sive', 'sub', 'sui', 'sum', 'super', 'suus', 
              'tam', 'tamen', 'trans', 'tu', 'tum', 'ubi', 'uel', 'uero', 'unus', 'ut']



for i in range(1,4):
    f = open(f'testing/latin/text/edit_text/ovid/ovid.artis{i}.txt','r')
    temp = [' et ',' ex ',' pro ', ' dum ', ' at ', ' in ', ' atque ', ' non ', ' ab ',
         ' ad ', ' de ', ' ut ', ' ac ', ' aut ', ' Sed ']
    a = set(temp)
    lst = []
    for line in f:
        for word in a:
            if word in line:
                line = line.replace(word,' ')
        lst.append(line)
    f.close()
    f = open(f'testing/latin/text/edit_text/ovid/ovid.artis{i}.txt','w')
    for line in lst:
        f.write(line)
    f.close()