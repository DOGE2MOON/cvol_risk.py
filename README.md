# cvol_risk.py
Returns a dataframe with maximum and expected value at risk for the cvi.finance Theta Vault using web3 calls and CoinGecko API

# Usage
CVOL_Risk(120) -> returns a dataframe with maximum vault risk (CVOL = $200) and expected vault risk (CVOL = $120) <br>
CVOL_Risk(120).to_csv('CVOL Risk.csv", encoding='utf-8') -> export to CSV file <br>
print(CVOL_Risk(120)) -> print to console <br>

