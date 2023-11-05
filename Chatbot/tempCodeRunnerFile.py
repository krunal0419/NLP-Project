if flag == 0:

    # making data frame
    data = pd.read_excel ("Gujarati_Dimensionality_Reduction.xlsx")
    i=0
    a = []

    # iterating the columns (symptoms-133)
    for col in data.columns:
        a.append(col) 
        i=i+1

    a.pop() # Detele last column which is for diseases
    l=len(a)
    s = [0] * l # Generate empty array s of size 132

    #symptoms=input('લક્ષણો દાખલ કરો  : ')

    #print(type(s))
    import nltk
    symptoms_word=symptoms
    for i in symptoms_word:
        s[a.index(i)]=1

    s=np.array(s)
    s=s.reshape(-1,1)
    s.shape
    s=s.T

    alldiseases = []
    for i in symptoms_word: 
        for k in range (41):
            if data[i][k] == 1:    
                alldiseases.append(data['રોગ'][k])  # All the disease of entered input

    def countfreq(alldiseases):
        freq_diseases = dict()

        for elem in alldiseases:
            # If element exists in dict then increment its value 
            if elem in freq_diseases:
                freq_diseases[elem] += 1
            else:
                freq_diseases[elem] = 1    

        freq_diseases = { key:value for key, value in freq_diseases.items() if value >= len(symptoms_word)}
        # Returns a dict of duplicate elements and thier frequency count
        return freq_diseases

    freq_diseases = countfreq(alldiseases)   
    freq_diseases = list(freq_diseases.items())
    commondiseases = np.array(freq_diseases)

    data = pd.DataFrame(commondiseases)
    data=data[data.columns[:-1]]
    commondiseases=data.to_numpy()

    print()
    if len(commondiseases) != 0:
        print("તમને થઈ શકે તેવા રોગની સંભાવનાઓ : ")
        alldiseases=commondiseases
        print(alldiseases)   
    else:
        x = np.array(alldiseases) 
        alldiseases=np.unique(x)
        print("તમને થઈ શકે તેવા રોગની સંભાવનાઓ : ")
        print(alldiseases)