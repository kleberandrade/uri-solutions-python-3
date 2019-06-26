hi, mi, hf, mf = map(int, input().split())

if hi == hf == mi == mf:
   hf += 24
elif hi == hf and mi >= mf:
   hf += 24
elif hi > hf:
   hf += 24
    
mit = hi * 60 + mi
mft = hf * 60 + mf

md = mft - mit

ht = md // 60
mt = md - ht * 60


print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(ht, mt))