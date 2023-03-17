#@title Interpolation Codeblock
#google colab use

from IPython.display import clear_output #for google colab use
clear_output() #for google colab use

T=(193.19,210.0,211.99,220.0,230.0,240.0,250.0,260.0,270.0,280.0,290.0,300.0) # Temp values from Thermodynamics book at the UO Book [F]
P=(10.0,14.13,14.695949,17.188,20.779,24.968,29.825,35.427,41.856,49.18,57.53,66.98) #Pressure values from steam table from the UO Book [psia]
H=(982.1,971.6,970.4,965.3,958.8,952.3,945.6,938.8,932.0,924.9,917.8,910.4) #Hvap values from steam table from the UO Book [btu/lbm]

tempMode=False
exit=False

while not exit:



#SELECT MODE
  while not exit:
      mode=input("Are you going to type in Temp or Pressure for interpolation?\n e.g. \"t\" or \"p\" to specify.\n You can also type \"exit\" to exit.") #Input our experimental pressure value in psig
      if mode.lower().startswith("t"): # temp input
        tempMode = True
        print("\n                 [Temperature Input Specified]\n")
        break
      elif mode.lower().startswith("p"): # pressure input
        tempMode = False
        print('\n                 [Pressure Input Specified]\n')
        break
      elif mode.lower().startswith("ex"): #exit command
        exit=True
        print("\n                     EXITING")
        clear_output() #for google colab use
        break
      else:
        print("\n                      Please say stuff like \"t\" for temp or \"p\" for pressure, or just \"exit\"\n")
        continue



#PRESSURE MODE
  while tempMode == False and not exit:
    try:
      expg=input("Enter the [psig] value to interpolate for: \n Type \"exit\" to exit. ") #Input our experimental pressure value in psig
      exp=float(expg)+14.695949
    except:
      if expg.lower().startswith("ex"): #exit command
        print("\n                     EXITING")
        exit=True
        clear_output() #for google colab use
        break
      print("\n                      Please input a number with or without decimals\n")
      continue
    else:
      print("\nYour input:", expg, "[psig], which is =",exp, "[psia]")
      for x in P:
        if max(P) < exp or min(P) > exp: #out of range exception
          print("\n                   Out of range for interpolation. Check your pressure, or add more steam pressure range values to the program.")
          print("                 Steam pressure should be at least 0 psig and maximum 52 psig~ish (at least for Natural Circulation). Are you sure?\n")
          break
        elif x >= exp: #find the one that "goes over" and interpolate using the values right before that value
          i=P.index(x)
          hInt=H[i-1]+(exp-P[i-1])/(P[i]-P[i-1])*(H[i] - H[i-1]) #calculate Hvap interpolation value
          tInt=T[i-1]+(exp-P[i-1])/(P[i]-P[i-1])*(T[i] - T[i-1]) #calculate Temp interpolation value
          print("\nInterpolation Result:\nInterpolated      @", round(exp,4) , "[psig]\n             Hvap =",round(hInt,4),"[BTU/lbm]\n             Temp =",round(tInt,4),"[F]\n\n")
          break  



#TEMP MODE
  while tempMode == True and not exit:
      try:
        exp=input("Enter the [F] value to interpolate for: \n Type \"exit\" to exit. ") #Input our experimental temp
        exp=float(exp)
      except:
        if exp.lower().startswith("ex"): #exit command
          print("\n                     EXITING")
          exit=True
          clear_output() #for google colab use
          break
        print("\n                      Please input a number with or without decimals\n")
        continue
      else:
        print("\nYour input:", exp, "[F]")
        for x in T:
          if max(T) < exp or min(T) > exp: #out of range exception
            print("\n                   Out of range for interpolation. Check your temp, or add more steam temp range values to the program.")
            print("                                   Temp should be at least 193.19 F and maximum 300.00 F. Are you sure?\n")
            break
          elif x >= exp: #find the one that "goes over" and interpolate using the values right before that value
            i=T.index(x)
            pInt=P[i-1]+(exp-T[i-1])/(T[i]-T[i-1])*(P[i] - P[i-1]) #calculate Pressure interpolation value
            hInt=H[i-1]+(exp-T[i-1])/(T[i]-T[i-1])*(H[i] - H[i-1]) #calculate Hvap interpolation value
            print("\nInterpolation Result:\nInterpolated      @", round(exp,4) , "[F]\n             Hvap =",round(hInt,4),"[BTU/lbm]\n             Pressure =",round(pInt,4),"[psiA]\n\n")
            break  
