def analyze_numbers(numbers:list) -> dict:
    result = {'even':0,'odd':0,'sum':0,'average':0,'max':0,'min':0}
    even=0
    odd= 0
    if len(numbers) != 0:
        def get_max(numbers:list)->int:
                Nmax= None 
                for number in numbers:
                    if Nmax is None or number > Nmax:
                     Nmax = number
                return Nmax

        def get_min(numbers:list)->int:
            Nmin= None 
            for number in numbers:
                if Nmin is None or number < Nmin:
                    Nmin = number
            return Nmin


        total = 0
        result['max'] = get_max(numbers)
        result['min'] = get_min(numbers)

        
        for number in numbers:
            total+=number
            if number %2 == 0:
                even +=1
                result['even']+=1
            else:
                odd +=1
                result['odd']+=1

        result['sum']=total

        result['average'] = total / len(numbers)
    else:
        raise ValueError('Empty list!')

    return result