import torch

class densnet121(torch.nn.Module):
    def __init__(self,freeze_layers_num=0):
        super(densnet121,self).__init__()
        self.densnet121 = torch.hub.load('pytorch/vision:v0.6.0', 'densenet121', pretrained=True)
        self.densnet121.classifier = torch.nn.Linear(1024, 2)
        if freeze_layers_num > 0 :
            for child in list(self.densnet121.children())[:-freeze_layers_num]:
                for param in child.parameters():
                    param.requires_grad = False


        
    def forward(self,x):
        x = self.densnet121(x)
        return x
    
class densnet169(torch.nn.Module):
    def __init__(self,freeze_layers_num=0):
        super(densnet169,self).__init__()
        self.densnet169 = torch.hub.load('pytorch/vision:v0.6.0', 'densenet169', pretrained=True)
        self.densnet169.classifier = torch.nn.Linear(1664, 2)
        if freeze_layers_num > 0 :
            for child in list(self.densnet169.children())[:-freeze_layers_num]:
                for param in child.parameters():
                    param.requires_grad = False     
    def forward(self,x):
        
        x = self.densnet169(x)
        return x