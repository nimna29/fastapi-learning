from pydantic import BaseModel

# Create object with feature names 
# ['variance', 'skewness', 'curtosis', 'entropy']
class BankNote(BaseModel):
    variance: float 
    skewness: float 
    curtosis: float 
    entropy: float