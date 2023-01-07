# cvol_risk.py
Returns a dataframe with maximum and expected value at risk for the cvi.finance Theta Vault using web3 calls and CoinGecko API

# Usage
CVOL_Risk(120, "YOUR_ADDRESS", True) -> returns a dataframe with maximum vault risk (CVOL = $200) and expected vault risk (CVOL = $120) <br>
CVOL_Risk(120, YOUR_ADDRESS, True).to_csv('CVOL Risk.csv", encoding='utf-8') -> export to CSV file <br>
print(CVOL_Risk(120, 0, False)) -> print only vault-level data to the console <br>

