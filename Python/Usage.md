# How to use "GetRandomCity.py":
> ### Step 1 (Importing):
>> With the "GetRandomCity.py" file in the same directory as your main Python file, in your main Python file, write the following code:
>> ```python
>> from GetRandomCity import GetRandomCity
>> ```

> ### Step 2 (Using the function):
>> When you're done [Step 1](https://github.com/danielhamen/25519-Worldwide-Cities/blob/main/Python/Usage.md#step-1-importing), you can now use the "GetRandomCity()" function. To use the function, write the following code in your main Python file:
>> ```python
>> Cities = GetRandomCity(1)
>> ```
>> Since the function returns a city, you will have to assign it to a variable before using it. 
>>> If you just want to test the program, you can simply write:
>>> ```python
>>> print(GetRandomCity(1))
>>> ```
>> The "1" in the argument is the amount of Cities you want to return. If you write < 1, the funciton will return all the Cities, but as a list as it is better for organization.
>> 
>> Now that you know how you can use the function, you can now create as many projects as you would like!

# The final code:
> ```python
> from GetRandomCity import GetRandomCity
> 
> Cities = GetRandomCity(1)
> 
> print(Cities)
> ```
> Output:
> ```python
> >>> Åndalsnes
> ```
> 
> 
> ## Or return multiple Cities:
> ```python
> from GetRandomCity import GetRandomCity
> 
> Cities = GetRandomCity(10)
> 
> print(Cities)
> ```
> Output:
> ```python
> >>> ['Laurens', 'Mezőhegyes', 'Toco', 'St. Albans', "Maarrat al-Nu'man", 'St. Marys', 'Blankenberge', 'Crawford', 'Nabagram', 'Rossie']
> ```
