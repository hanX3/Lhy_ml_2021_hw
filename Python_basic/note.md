# basic
print('%02d-%02d' % (3, 1)) ==> 3-1

# list

## List Comprehension
l = [x * x for x in range(1, 11) if x % 2 == 0]
==> [4, 16, 36, 64, 100]

## slice
### one dimension list, two dimension list can look as one dimension list
l[0:3], first 3 element
l[:3],  first 3 element
l[-2:], last 2 element

### two dimension list, from numpy module
l[:,0], get first element of all rows
l[:,1], get second element of all rows
l[:,m:n], get m to n-1 coloum elements of all rows

# dic
d = {key1 : value1, key2 : value2 }

# csv

csv.reader(csvfile), read csv file and save each row data into a list

# numpy



# torch
## mean()
a.mean(dim=0, keepdim=True), get mean value in dimension 0, and keep output dimension.
torch.Size(4, 53)  ==> torch.Size(1, 53)
a.mean(dim=1, keepdim=True), get mean value in dimension 1, and keep output dimension.
torch.Size(4, 53) ==> torch.Size(4, 1)

## shape
return dimension of tensor

## Optimizer
optimizer = optim.SGD(model.parameters(), lr = 0.01, momentum=0.9)
optimizer = getattr(torch.optim, 'SGD')(model.parameters(), **config)
