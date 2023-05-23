import numpy as np

def replace_words(sent):
  sent = sent.lower()
  if " more " in sent:
    return sent.replace( " more " , " less " )
  elif " less " in sent:
    return sent.replace( " less " , " more " )
  elif " positive " in sent:
    return sent.replace( " positive " , " negative " )
  elif " negative " in sent:
    return sent.replace( " negative " , " positive " )
  elif " yes " in sent:
    return sent.replace( " yes " , " no " )
  elif " no " in sent:
    return sent.replace( " no " , " yes " )
  elif " unable " in sent:
    return sent.replace( " unable " , " able " )
  elif " able " in sent:
    return sent.replace( " able " , " unable " )
  elif " increase " in sent:
    return sent.replace( " increase " , " decrease " )
  elif " decrease " in sent:
    return sent.replace( " decrease " , " increase " )
  elif " sales " in sent:
    return sent.replace(" sales ", " buy ")
  elif " sale " in sent:
    return sent.replace( " sale " , " buy " )
  elif " buy " in sent:
    return sent.replace( " buy " , " sale " )
  elif " best " in sent:
    return sent.replace( " best " , " worst " )
  elif " worst " in sent:
    return sent.replace( " worst " , " best " )
  elif " larger " in sent:
    return sent.replace( " larger " , " smaller " )
  elif " smaller " in sent:
    return sent.replace( " smaller " , " larger " )
  elif " large " in sent:
    return sent.replace( " large " , " small " )
  elif " small " in sent:
    return sent.replace( " small " , " large " )
  elif " good " in sent:
    return sent.replace( " good " , " bad " )
  elif " bad " in sent:
    return sent.replace( " bad " , " good " )
  elif " high " in sent:
    return sent.replace( " high " , " low " )
  elif " low " in sent:
    return sent.replace( " low " , " high " )
  elif " down " in sent:
    return sent.replace( " down " , " up " )
  elif " up " in sent:
    return sent.replace( " up " , " down " )
  elif " dislike " in sent:
    return sent.replace( " dislike " , " like " )
  elif " like " in sent:
    return sent.replace( " like " , " dislike " )
  elif " right " in sent:
    return sent.replace( " right " , " wrong " )
  elif " wrong " in sent:
    return sent.replace( " wrong " , " right " )
  elif " a lot of " in sent:
    return sent.replace( " a lot of " , " few " )
  elif " many " in sent:
    return sent.replace( " many " , " few " )
  elif " few " in sent:
    return sent.replace( " few " , " many " )
  elif " little " in sent:
    return sent.replace( " little " , " much " )
  elif " much " in sent:
    return sent.replace( " much " , " little " )
  elif " disbelieve " in sent:
    return sent.replace( " disbelieve " , " believe " )
  elif " believe " in sent:
    return sent.replace( " believe " , " disbelieve " )
  elif " better " in sent:
    return sent.replace( " better " , " worse " )
  elif " worse " in sent:
    return sent.replace( " worse " , " better " )
  elif " revenue " in sent:
    return sent.replace( " revenue " , " expense " )
  elif " expense " in sent:
    return sent.replace( " expense " , " revenue " )
  elif " abandon " in sent:
    return sent.replace( " abandon " , " remain " )
  elif " remain " in sent:
    return sent.replace( " remain " , " abandon " )
  elif " continuing " in sent:
    return sent.replace( " continuing " , " stopping " )
  elif " stopping " in sent:
    return sent.replace( " stopping " , " continuing " )
  elif " continue " in sent:
    return sent.replace( " continue " , " stop " )
  elif " stop " in sent:
    return sent.replace( " stop " , " continue " )
  elif " approve " in sent:
    return sent.replace( " approve " , " refuse " )
  elif " refuse " in sent:
    return sent.replace( " refuse " , " approve " )
  elif " grew " in sent:
    return sent.replace( " grew " , " decayed " )
  elif " decayed " in sent:
    return sent.replace( " decayed " , " grew " )
  elif " decay " in sent:
    return sent.replace( " decay " , " grow " )
  elif " growth " in sent:
    return sent.replace( " growth " , " decay " )
  elif " grow " in sent:
    return sent.replace( " grow " , " decay " )
  elif " improvement " in sent:
    return sent.replace( " improvement " , " degeneration " )
  elif " degeneration " in sent:
    return sent.replace( " degeneration " , " improvement " )
  elif " improve " in sent:
    return sent.replace( " improve " , " degenerate " )
  elif " degenerate " in sent:
    return sent.replace( " degenerate " , " improve " )
  elif " focus " in sent:
    return sent.replace( " focus " , " ignore " )
  elif " ignore " in sent:
    return sent.replace( " ignore " , " focus " )
  elif " major " in sent:
    return sent.replace( " major " , " minor " )
  elif " minor " in sent:
    return sent.replace( " minor " , " major " )
  elif " strong " in sent:
    return sent.replace( " strong " , " weak " )
  elif " weak " in sent:
    return sent.replace( " weak " , " strong " )
  elif " full " in sent:
    return sent.replace( " full " , " empty " )
  elif " empty " in sent:
    return sent.replace( " empty " , " full " )
  elif " start " in sent:
    return sent.replace( " start " , " end " )
  elif " end " in sent:
    return sent.replace( " end " , " start " )
  elif " progress " in sent:
    return sent.replace( " progress " , " decline " )
  elif " decline " in sent:
    return sent.replace( " decline " , " progress " )
  elif " earnings " in sent:
    return sent.replace( " earnings " , " cost " )
  elif " cost " in sent:
    return sent.replace( " cost " , " earnings " )
  elif " well " in sent:
    return sent.replace( " well " , " badly " )
  elif " badly " in sent:
    return sent.replace( " badly " , " well " )
  elif " expect " in sent:
    return sent.replace( " expect " , " dismiss " )
  elif " dismiss " in sent:
    return sent.replace( " dismiss " , " expect " )
  elif " over " in sent:
    return sent.replace( " over " , " below " )
  elif " below " in sent:
    return sent.replace( " below " , " over " )
  elif " back " in sent:
    return sent.replace( " back " , " forward " )
  elif " forward " in sent:
    return sent.replace( " forward " , " back " )
  elif " margin " in sent:
    return sent.replace( " margin " , " loss " )
  elif " profit " in sent:
    return sent.replace( " profit " , " loss " )
  elif " benefits " in sent:
    return sent.replace( " benefits " , " loss " )
  elif " income " in sent:
    return sent.replace( " income " , " loss " )
  elif " loss " in sent:
    return sent.replace( " loss " , " profit " )
  elif " benefit " in sent:
    return sent.replace( " benefit " , " harm " )
  elif " harm " in sent:
    return sent.replace( " harm " , " benefit " )
  elif " slightly " in sent:
    return sent.replace( " slightly " , " completely " )
  elif " completely " in sent:
    return sent.replace( " completely " , " slightly " )
  elif " most " in sent:
    return sent.replace( " most " , " least " )
  elif " least " in sent:
    return sent.replace( " least " , " most " )
  elif " add " in sent:
    return sent.replace( " add " , " decrease " )
  elif " change " in sent:
    return sent.replace( " change " , " unchange " )
  elif " opportunities " in sent:
    return sent.replace( " opportunities " , " changes " )
  elif " opportunity " in sent:
    return sent.replace( " opportunity " , " change " )
  elif " within " in sent:
    return sent.replace( " within " , " without " )
  elif " without " in sent:
    return sent.replace( " without " , " with " )
  elif " with " in sent:
    return sent.replace( " with " , " without " )
  else:
      return sent

def make_neg():
    test_list = np.load("earnings_call_3days.npy")
    for i in test_list:
        # print(i)
        if i[1] == '1.0':
            i[1] = '0.0'
        else:
            i[1] = '1.0'
        text = i[3].replace('\n', '.\n')
        text = text.split('\n')
        neg_text = ''
        for j in text:
            j = replace_words(j)
            neg_text += j
            neg_text += " "
        i[3] = neg_text.replace('. ','\n')
        # print(i)
    np.save("neg_earnings_call_3days.npy", test_list)


if __name__ == "__main__":
    make_neg()
