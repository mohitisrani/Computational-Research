import os
import time


x=0
data=open('ACFDATA','w')

for comp in os.listdir('.'):
    if os.path.isdir(comp):
#        x=x+1
#        print x
        y=raw_input("Check ACF.dat for "+comp+"?(y/n)")
        if y=="y":
            os.chdir('/ufrc/hennig/misrani/ChemSub/Al2Te3/'+comp)
            l=-1
            Mchg=0
            Mdiff=0
            Xchg=0
            Xdiff=0
            os.system('grep ZVAL OUTCAR >ZVAL')
            ZVAL=open('ZVAL').readlines()
            #print ZVAL
            ZVAL1=ZVAL[0].split()
            ZVAL2=ZVAL[1].split()
            M=ZVAL1[5]
            X=ZVAL2[5]
            data.write("    "+comp+"\n")
            lines=open('ACF.dat','r').readlines()
            for line in lines:
                if l>=1 and l<=8:
                    chg=float(line.split()[4])
                    Mchg=Mchg+chg
                    diff=float(line.split()[4])-float(M)
                    Mdiff=Mdiff+diff
                    lc = str(diff)
                    data.write(line.rstrip()+'   '+M+'   '+lc+'\n')
                elif l>=9 and l<=20:
                    chg= float(line.split()[4])
                    Xchg=Xchg+chg
                    diff=float(line.split()[4])-float(X)
                    Xdiff=Xdiff+diff
                    lc=str(diff)
                    data.write(line.rstrip()+'   '+X+'   '+lc+'\n')
                else :
                    data.write(line)
                l=l+1
            data.write('   M - - - '+str(Mchg/8)+' - - - '+str(Mdiff/8)+'\n   X - - - '+str(Xchg/12)+' - - -  '+str(Xdiff/12)+'\n\n\n')
#            y=raw_input("Proceed?(y/n)")
 #           if y=="y":
 #           os.system('bader CHGCAR -ref CHGCAR_sum')
  #          time.sleep(1)

            os.chdir('../')
        else:continue
    else:continue
data.close()
#print x, "jobs estimated"

