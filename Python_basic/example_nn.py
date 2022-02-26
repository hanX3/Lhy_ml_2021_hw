#!/usr/bin/env python3

import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torch.utils.data import DataLoader
import torchvision.datasets as datasets
import torchvision.transforms as transforms


# create fully connect network
class NN(nn.Module):
  def __init__(self, input_size, num_classes):
    super(NN, self).__init__()
    self.fc1 = nn.Linear(input_size, 50)
    self.fc2 = nn.Linear(50, num_classes)

  def forward(self, x):
    x = self.fc1(x)
    x = F.relu(x)
    x = self.fc2(x)
    return x

# test network
'''
model = NN(784, 10)
x = torch.randn(64, 784)
print(model(x).shape)
'''

# set device
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# hyperparameter
input_size = 784
num_classes = 10
learning_rate = 0.001
batch_size = 64
num_epochs = 1

# loda data
train_dataset = datasets.MNIST(root='../../data/', train=True, transform=transforms.ToTensor(), download=True)
train_loader = DataLoader(dataset=train_dataset, batch_size=batch_size, shuffle=True)
test_dataset = datasets.MNIST(root='../../data/', train=False, transform=transforms.ToTensor(), download=True)
test_loader = DataLoader(dataset=test_dataset, batch_size=batch_size, shuffle=True)

# initialize network
model = NN(input_size=input_size, num_classes=num_classes).to(device)

# loss and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

# train network
for eponch in range(num_epochs):
  for batch_index, (data, targets) in enumerate(train_loader):
    # get data to cuda if possible
    data = data.to(device=device)
    targets = targets.to(device=device)
    
    # get to correct shape
    # print(data.shape)
    data = data.reshape(data.shape[0], -1)
    # print(data.shape)

    # forward
    scores = model(data)
    loss = criterion(scores, targets)
    
    # backward
    optimizer.zero_grad()
    loss.backward()

    # gradient descent or adam step
    optimizer.step()

# check accuracy on training & test to see how good our model
def check_accuracy(loader, model):
  if loader.dataset.train:
    print("checking accuracy on training data")
  else:
    print("checking accuracy on test data")

  num_correct = 0
  num_samples = 0
  model.eval()

  with torch.no_grad():
    for x, y in loader:
      x = x.to(device=device)
      y = y.to(device=device)
      x = x.reshape(x.shape[0], -1)

      scores = model(x)
      _, predictions = scores.max(1)
      num_correct += (predictions == y).sum()
      num_samples += predictions.size(0)

  print(f'Got {num_correct} / {num_samples} with accuracy {float(num_correct)/float(num_samples)*100:.2f}')

  model.train()

check_accuracy(train_loader, model)
check_accuracy(test_loader, model)
