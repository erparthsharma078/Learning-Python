
def generate_no(n):
    for i in range(n):
        yield i
n=int(input("Enter any number : ")) 
res=generate_no(n)   
print(res)
print(next(res)) 
print("Hello....... ")
print("Welcome......")
print(next(res))   


# l=list[range(10000)]
# print(l)