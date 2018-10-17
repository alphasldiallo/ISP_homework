
import operator
import enchant


#f = open('ciphertext.txt', 'r')
#ctext = f.read()
ctext ="Bm bl ngdghpg ahp xyyxvmbox max Vtxltk vbiaxk ptl tm max mbfx, unm bm bl ebdxer mh atox uxxg kxtlhgtuer lxvnkx, ghm extlm uxvtnlx fhlm hy Vtxltk'l xgxfbxl phnew atox uxxg beebmxktmx tgw hmaxkl phnew atox tllnfxw matm max fxlltzxl pxkx pkbmmxg bg tg ngdghpg yhkxbzg etgzntzx. Maxkx bl gh kxvhkw tm matm mbfx hy tgr mxvagbjnxl yhk max lhenmbhg hy lbfiex lnulmbmnmbhg vbiaxkl. Max xtkebxlm lnkobobgz kxvhkwl wtmx mh max 9ma vxgmnkr phkdl hy Te-Dbgwb bg max Tktu phkew pbma max wblvhoxkr hy ykxjnxgvr tgterlbl."
letter_frequency_english =  {'e','t','a','o','i','n','s','r','h','d','l','u','c','m','f','y','w','g','p','b','v','k','x','q','j','z'}
alphabet =  {'a':'0','b':'1','c':'2','d':'3','e':'4','f':'5','g':'6','h':'7','i':'8','j':'9','k':'10','l':'11','m':'12','n':'13','o':'14','p':'15','q':'16','r':'17','s':'18','t':'19','u':'20','v':'21','w':'22','x':'23','y':'24','z':'25'}

alphabet_array = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

alphabet_1 =  ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
c_special =['!', ''" "'','"', '#', '$', '%', '&', '(',')', '*' ,'+',',', '_','.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':',';','=', '?', '@', '[', ']','', '^', '_', '{', '|', '}', '~',"'", '-']
dico_ct ={}
result1 = ()
count = 0
list_decipher = []
print ("alphabet", alphabet_array[5])

for letter in ctext.lower():
   if letter not in c_special:
       if letter not in dico_ct:
          dico_ct[letter] = 1
       else:
          dico_ct[letter] += 1
print(dico_ct)

# Order the elements of the list
result= sorted(dico_ct.items(), key=operator.itemgetter(1), reverse=True)
print("result",(result[0]))

list=[]
for item in result[0]:
    list.append(item)
    print("item",list)
print ("list",list[0])
print (int(alphabet[(list[0])]))
# C = (m + b) mod 26
# b =  C - m mod 26
# C = position de la lettre qui plus se repete    m = position de la lettre qui stadistiquement se repete le plus dans l'alphabet anglais

for lk in alphabet:
    lettre_key = alphabet[lk]
    print("lettre_key",lettre_key)
    print("LK", lk)

    b = ((int(alphabet[list[0]])) - int(lettre_key)) % 26
    print("B = ", b)
#print ("position ", alphabet_array.index("f"))

#for i in alphabet_array:
#    b = ((int(alphabet[list[0]]))-(int(alphabet(alphabet_array[i]))))%26
 #   b = 19
    #print ("B = ",b)


    result1 = alphabet_1[b:] + alphabet_1[:b]
    print("result1", result1)

    decipher = dict(zip(result1,alphabet))
    print ("decipher",decipher)

    translatable = str.maketrans(decipher)
    print(str.translate(ctext.lower(), translatable))

    words_tr = (str.translate(ctext.lower(), translatable))
    print(words_tr.split(" "))
    list_decipher = (words_tr.split(" "))
    print("cantidad palabras",len(list_decipher))
    count = 0

    for candidate_word in list_decipher:
       # print ("candidate_word",candidate_word)
        d = enchant.Dict("en_US")
        answer = d.check(candidate_word)
       # print("answer",answer)
        if answer == True:
           count += 1
           print("count", count)
           if count > (len(list_decipher)-10):
            break

    print("words_tr",words_tr)





