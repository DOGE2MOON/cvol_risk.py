import json
import os
from web3 import Web3
import sys
import pandas as pd
from pycoingecko import CoinGeckoAPI

def CVOL_Risk(expected_value, address, user_data):
	output = pd.DataFrame()
	expected_value = float(expected_value)
	cg = CoinGeckoAPI()
	web3 = Web3(Web3.HTTPProvider('https://arb1.arbitrum.io/rpc'))

	CVOL_Address = '0x8096aD3107715747361acefE685943bFB427C722'
	SLP_Address = '0xeDE0CE8cdc65bcF6422f3Afb9d7cDb3e59C09658'
	T_CVOL_LP_Address = '0xFDeB59a2B4891ea17610EE38665249acC9FCC506'

	T_CVOL_LP_Proxy_ABI = json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"requestId","type":"uint256"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":false,"internalType":"uint256","name":"totalUSDCAmount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"platformLiquidityAmount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"dexVolTokenUSDCAmount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"dexVolTokenAmount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"dexUSDCAmount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"mintedThetaTokens","type":"uint256"}],"name":"FulfillDeposit","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"requestId","type":"uint256"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":false,"internalType":"uint256","name":"totalUSDCAmount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"platformLiquidityAmount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"dexVolTokenAmount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"dexUSDCVolTokenAmount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"dexUSDCAmount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"burnedThetaTokens","type":"uint256"}],"name":"FulfillWithdraw","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint8","name":"version","type":"uint8"}],"name":"Initialized","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"requestId","type":"uint256"},{"indexed":false,"internalType":"uint8","name":"requestType","type":"uint8"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"liquidator","type":"address"},{"indexed":false,"internalType":"uint256","name":"tokenAmount","type":"uint256"}],"name":"LiquidateRequest","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"requestId","type":"uint256"},{"indexed":false,"internalType":"uint8","name":"requestType","type":"uint8"},{"indexed":false,"internalType":"uint256","name":"tokenAmount","type":"uint256"},{"indexed":false,"internalType":"uint32","name":"targetTimestamp","type":"uint32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":false,"internalType":"uint256","name":"totalUSDCBalance","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"totalSupply","type":"uint256"}],"name":"SubmitRequest","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[],"name":"DEPOSIT_REQUEST_TYPE","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"MAX_PERCENTAGE","outputs":[{"internalType":"uint16","name":"","type":"uint16"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"PRECISION_DECIMALS","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"UNISWAP_REMOVE_MAX_FEE_PERCENTAGE","outputs":[{"internalType":"uint16","name":"","type":"uint16"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"WITHDRAW_REQUEST_TYPE","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"depositCap","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"depositHoldingsPercentage","outputs":[{"internalType":"uint16","name":"","type":"uint16"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"extraLiqidityPercentage","outputs":[{"internalType":"uint16","name":"","type":"uint16"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_requestId","type":"uint256"}],"name":"fulfillDepositRequest","outputs":[{"internalType":"uint256","name":"thetaTokensMinted","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_requestId","type":"uint256"}],"name":"fulfillWithdrawRequest","outputs":[{"internalType":"uint256","name":"tokenWithdrawnAmount","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"fulfiller","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getReserves","outputs":[{"internalType":"uint256","name":"volTokenAmount","type":"uint256"},{"internalType":"uint256","name":"usdcAmount","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"initialTokenToThetaTokenRate","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_initialTokenToThetaTokenRate","type":"uint256"},{"internalType":"contract IPlatform","name":"_platform","type":"address"},{"internalType":"contract IVolatilityToken","name":"_volToken","type":"address"},{"internalType":"contract IRewardRouter","name":"_rewardRouter","type":"address"},{"internalType":"contract IERC20Upgradeable","name":"_token","type":"address"},{"internalType":"contract IUniswapV2Router02","name":"_router","type":"address"},{"internalType":"string","name":"_lpTokenName","type":"string"},{"internalType":"string","name":"_lpTokenSymbolName","type":"string"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"lastDepositTimestamp","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_requestId","type":"uint256"}],"name":"liquidateRequest","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"liquidationPeriod","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"lockupPeriod","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"maxMinRequestIncrements","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"minDepositAmount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"minDexPercentageAllowed","outputs":[{"internalType":"uint16","name":"","type":"uint16"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"minPoolSkewPercentage","outputs":[{"internalType":"uint16","name":"","type":"uint16"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"minRequestId","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"minWithdrawAmount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"nextRequestId","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"platform","outputs":[{"internalType":"contract IPlatform","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"rebalance","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"requestDelay","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"requests","outputs":[{"internalType":"uint8","name":"requestType","type":"uint8"},{"internalType":"uint168","name":"tokenAmount","type":"uint168"},{"internalType":"uint32","name":"targetTimestamp","type":"uint32"},{"internalType":"address","name":"owner","type":"address"},{"internalType":"bool","name":"shouldStake","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"rewardRouter","outputs":[{"internalType":"contract IRewardRouter","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"router","outputs":[{"internalType":"contract IUniswapV2Router02","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_newDepositCap","type":"uint256"}],"name":"setDepositCap","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_newDepositHoldingsPercentage","type":"uint16"}],"name":"setDepositHoldings","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_newFulfiller","type":"address"}],"name":"setFulfiller","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_newExtraLiquidityPercentage","type":"uint16"},{"internalType":"uint16","name":"_minDexPercentageAllowed","type":"uint16"}],"name":"setLiquidityPercentages","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_newMinDepositAmount","type":"uint256"},{"internalType":"uint256","name":"_newMinWithdrawAmount","type":"uint256"}],"name":"setMinAmounts","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_newMinPoolSkewPercentage","type":"uint16"}],"name":"setMinPoolSkew","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_newLockupPeriod","type":"uint256"},{"internalType":"uint256","name":"_newLiquidationPeriod","type":"uint256"}],"name":"setPeriods","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_newRequestDelay","type":"uint256"}],"name":"setRequestDelay","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"contract IRewardRouter","name":"_rewardRouter","type":"address"}],"name":"setRewardRouter","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint168","name":"_tokenAmount","type":"uint168"}],"name":"submitDepositRequest","outputs":[{"internalType":"uint256","name":"requestId","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint168","name":"_thetaTokenAmount","type":"uint168"}],"name":"submitWithdrawRequest","outputs":[{"internalType":"uint256","name":"requestId","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"token","outputs":[{"internalType":"contract IERC20Upgradeable","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalBalance","outputs":[{"internalType":"uint256","name":"balance","type":"uint256"},{"internalType":"uint256","name":"usdcPlatformLiquidity","type":"uint256"},{"internalType":"uint256","name":"intrinsicDEXVolTokenBalance","type":"uint256"},{"internalType":"uint256","name":"volTokenPositionBalance","type":"uint256"},{"internalType":"uint256","name":"dexUSDCAmount","type":"uint256"},{"internalType":"uint256","name":"dexVolTokensAmount","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalDepositRequestsAmount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalHoldingsAmount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalVaultLeveragedAmount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"vaultPositionUnits","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"volToken","outputs":[{"internalType":"contract IVolatilityToken","name":"","type":"address"}],"stateMutability":"view","type":"function"}]')
	CVOL_Proxy_ABI = json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"requestId","type":"uint256"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":false,"internalType":"uint256","name":"tokenAmountBeforeFees","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"tokenAmount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"burnedTokens","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"closePositionFee","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"closingPremiumFee","type":"uint256"}],"name":"Burn","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"requestId","type":"uint256"},{"indexed":false,"internalType":"uint8","name":"requestType","type":"uint8"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":false,"internalType":"uint256","name":"fulfillFeesAmount","type":"uint256"},{"indexed":false,"internalType":"bool","name":"isAborted","type":"bool"},{"indexed":false,"internalType":"bool","name":"useKeepers","type":"bool"},{"indexed":false,"internalType":"bool","name":"keepersCalled","type":"bool"},{"indexed":true,"internalType":"address","name":"fulfiller","type":"address"},{"indexed":false,"internalType":"uint32","name":"fulfillTimestamp","type":"uint32"}],"name":"FulfillRequest","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint8","name":"version","type":"uint8"}],"name":"Initialized","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"requestId","type":"uint256"},{"indexed":false,"internalType":"uint8","name":"requestType","type":"uint8"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"liquidator","type":"address"},{"indexed":false,"internalType":"uint256","name":"findersFeeAmount","type":"uint256"},{"indexed":false,"internalType":"bool","name":"useKeepers","type":"bool"},{"indexed":false,"internalType":"uint32","name":"liquidateTimestamp","type":"uint32"}],"name":"LiquidateRequest","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"requestId","type":"uint256"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":false,"internalType":"uint256","name":"tokenAmount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"positionedTokenAmount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"mintedTokens","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"openPositionFee","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"buyingPremiumFee","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"epoch","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"prevScalingFactor","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"newScalingFactor","type":"uint256"}],"name":"Rebase","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"requestId","type":"uint256"},{"indexed":false,"internalType":"uint8","name":"requestType","type":"uint8"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":false,"internalType":"uint256","name":"tokenAmount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"submitFeesAmount","type":"uint256"},{"indexed":false,"internalType":"uint32","name":"requestTimestamp","type":"uint32"},{"indexed":false,"internalType":"uint32","name":"targetTimestamp","type":"uint32"},{"indexed":false,"internalType":"bool","name":"useKeepers","type":"bool"},{"indexed":false,"internalType":"uint16","name":"maxBuyingPremiumFeePercentage","type":"uint16"}],"name":"SubmitRequest","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[],"name":"BURN_REQUEST_TYPE","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"CVI_DECIMALS_FIX","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"DELTA_PRECISION_DECIMALS","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"MAX_PERCENTAGE","outputs":[{"internalType":"uint16","name":"","type":"uint16"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"MINT_REQUEST_TYPE","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"PRECISION_DECIMALS","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"SCALING_FACTOR_DECIMALS","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"name_","type":"string"},{"internalType":"string","name":"symbol_","type":"string"},{"internalType":"uint8","name":"decimals_","type":"uint8"}],"name":"__ElasticToken_init","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"owner_","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"who","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"who","type":"address"}],"name":"balanceOfUnderlying","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint168","name":"burnAmount","type":"uint168"}],"name":"burnTokens","outputs":[{"internalType":"uint256","name":"tokenAmount","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"cappedRebase","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"cviOracle","outputs":[{"internalType":"contract ICVIOracle","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"deviationPerSingleRebaseLag","outputs":[{"internalType":"uint16","name":"","type":"uint16"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"feesCalculator","outputs":[{"internalType":"contract IFeesCalculator","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"feesCollector","outputs":[{"internalType":"contract IFeesCollector","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_requestId","type":"uint256"},{"internalType":"bool","name":"_keepersCalled","type":"bool"}],"name":"fulfillBurnRequest","outputs":[{"internalType":"uint256","name":"tokensReceived","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_requestId","type":"uint256"},{"internalType":"uint16","name":"_maxBuyingPremiumFeePercentage","type":"uint16"},{"internalType":"bool","name":"_keepersCalled","type":"bool"}],"name":"fulfillMintRequest","outputs":[{"internalType":"uint256","name":"tokensMinted","type":"uint256"},{"internalType":"bool","name":"success","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"fulfiller","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"initSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"initialTokenToLPTokenRate","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contract IERC20Upgradeable","name":"_token","type":"address"},{"internalType":"string","name":"_lpTokenName","type":"string"},{"internalType":"string","name":"_lpTokenSymbolName","type":"string"},{"internalType":"uint8","name":"_leverage","type":"uint8"},{"internalType":"uint256","name":"_initialTokenToVolTokenRate","type":"uint256"},{"internalType":"contract IPlatform","name":"_platform","type":"address"},{"internalType":"contract IFeesCollector","name":"_feesCollector","type":"address"},{"internalType":"contract IFeesCalculator","name":"_feesCalculator","type":"address"},{"internalType":"contract IRequestFeesCalculator","name":"_requestFeesCalculator","type":"address"},{"internalType":"contract ICVIOracle","name":"_cviOracle","type":"address"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"keepersFeeVaultAddress","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"leverage","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_requestId","type":"uint256"}],"name":"liquidateRequest","outputs":[{"internalType":"uint256","name":"findersFeeAmount","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"maxDeviationPercentage","outputs":[{"internalType":"uint16","name":"","type":"uint16"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"maxMinRequestIncrements","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"maxScalingFactor","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"maxTotalRequestsAmount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"minDeviationPercentage","outputs":[{"internalType":"uint16","name":"","type":"uint16"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"minKeepersBurnAmount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"minKeepersMintAmount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"minRequestId","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint168","name":"tokenAmount","type":"uint168"}],"name":"mintTokens","outputs":[{"internalType":"uint256","name":"mintedTokens","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"minter","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"nextRequestId","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"platform","outputs":[{"internalType":"contract IPlatform","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"rebaseCVI","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"rebaser","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"requestFeesCalculator","outputs":[{"internalType":"contract IRequestFeesCalculator","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"requests","outputs":[{"internalType":"uint8","name":"requestType","type":"uint8"},{"internalType":"uint168","name":"tokenAmount","type":"uint168"},{"internalType":"uint16","name":"timeDelayRequestFeesPercent","type":"uint16"},{"internalType":"uint16","name":"maxRequestFeesPercent","type":"uint16"},{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint32","name":"requestTimestamp","type":"uint32"},{"internalType":"uint32","name":"targetTimestamp","type":"uint32"},{"internalType":"bool","name":"useKeepers","type":"bool"},{"internalType":"uint16","name":"maxBuyingPremiumFeePercentage","type":"uint16"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"scalingFactor","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contract ICVIOracle","name":"_newCVIOracle","type":"address"}],"name":"setCVIOracle","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bool","name":"_newCappedRebase","type":"bool"}],"name":"setCappedRebase","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_newDeviationPercentagePerSingleRebaseLag","type":"uint16"},{"internalType":"uint16","name":"_newMinDeviationPercentage","type":"uint16"},{"internalType":"uint16","name":"_newMaxDeviationPercentage","type":"uint16"}],"name":"setDeviationParameters","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"contract IFeesCalculator","name":"_newFeesCalculator","type":"address"}],"name":"setFeesCalculator","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"contract IFeesCollector","name":"_newCollector","type":"address"}],"name":"setFeesCollector","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_fulfiller","type":"address"}],"name":"setFulfiller","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_newKeepersFeeVaultAddress","type":"address"}],"name":"setKeepersFeeVaultAddress","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_newMaxMinRequestIncrements","type":"uint256"}],"name":"setMaxMinRequestIncrements","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_maxTotalRequestsAmount","type":"uint256"}],"name":"setMaxTotalRequestsAmount","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_newMinKeepersMintAmount","type":"uint256"},{"internalType":"uint256","name":"_newMinKeepersBurnAmount","type":"uint256"}],"name":"setMinKeepersAmounts","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_newMinRequestId","type":"uint256"}],"name":"setMinRequestId","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_newMinter","type":"address"}],"name":"setMinter","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"contract IPlatform","name":"_newPlatform","type":"address"}],"name":"setPlatform","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_rebaser","type":"address"}],"name":"setRebaser","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"contract IRequestFeesCalculator","name":"_newRequestFeesCalculator","type":"address"}],"name":"setRequestFeesCalculator","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bool","name":"_verifyTotalRequestsAmount","type":"bool"}],"name":"setVerifyTotalRequestsAmount","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint168","name":"_tokenAmount","type":"uint168"},{"internalType":"uint32","name":"_timeDelay","type":"uint32"}],"name":"submitBurnRequest","outputs":[{"internalType":"uint256","name":"requestId","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint168","name":"_tokenAmount","type":"uint168"},{"internalType":"uint32","name":"_timeDelay","type":"uint32"}],"name":"submitKeepersBurnRequest","outputs":[{"internalType":"uint256","name":"requestId","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint168","name":"_tokenAmount","type":"uint168"},{"internalType":"uint32","name":"_timeDelay","type":"uint32"},{"internalType":"uint16","name":"_maxBuyingPremiumFeePercentage","type":"uint16"}],"name":"submitKeepersMintRequest","outputs":[{"internalType":"uint256","name":"requestId","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint168","name":"_tokenAmount","type":"uint168"},{"internalType":"uint32","name":"_timeDelay","type":"uint32"}],"name":"submitMintRequest","outputs":[{"internalType":"uint256","name":"requestId","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"token","outputs":[{"internalType":"contract IERC20Upgradeable","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalRequestsAmount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"unerlyingValue","type":"uint256"}],"name":"underlyingToValue","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"value","type":"uint256"}],"name":"valueToUnderlying","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"verifyTotalRequestsAmount","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"}]')
	
	CVOL_Contract = web3.eth.contract(address=CVOL_Address, abi=CVOL_Proxy_ABI)
	T_CVOL_LP_Contract = web3.eth.contract(address=T_CVOL_LP_Address, abi=T_CVOL_LP_Proxy_ABI)

	decimals = CVOL_Contract.functions.decimals().call() # can be hardcoded to 18
	CVOL_Total_Supply = CVOL_Contract.functions.totalSupply().call() / 10**decimals
	SLP_CVOL_Balance = CVOL_Contract.functions.balanceOf(SLP_Address).call() / 10**decimals

	CVOL_Held = CVOL_Total_Supply - SLP_CVOL_Balance
	CVOL_Current_Price = cg.get_price(ids="crypto-volatility-token", vs_currencies='usd')['crypto-volatility-token']['usd']
	Max_Vault_Risk = CVOL_Held * (200 - CVOL_Current_Price)
	Expected_Vault_Risk = CVOL_Held * (expected_value - CVOL_Current_Price)

	T_CVOL_LP_USDC_Balance = T_CVOL_LP_Contract.functions.totalBalance().call()
	T_CVOL_LP_USDC_Balance = T_CVOL_LP_USDC_Balance[0] / 10**6 # usdc contract uses 6 decimals
	T_CVOL_LP_Supply = T_CVOL_LP_Contract.functions.totalSupply().call() / 10**18
	Theta_Vault_Ratio = T_CVOL_LP_USDC_Balance / T_CVOL_LP_Supply

	if user_data == True:
		address = Web3.toChecksumAddress(address)
		User_T_CVOL_LP_Balance = T_CVOL_LP_Contract.functions.balanceOf(address).call() / 10**18
		User_USDC_Balance = User_T_CVOL_LP_Balance * Theta_Vault_Ratio
		User_Pool_Ownership = User_USDC_Balance / T_CVOL_LP_USDC_Balance
		Max_User_Risk = User_Pool_Ownership * Max_Vault_Risk
		Expected_User_Risk = User_Pool_Ownership * Expected_Vault_Risk

		output.at["User USDC Balance", "USD"] = round(User_USDC_Balance,2)
		output.at["Max User Risk", "USD"] = round(Max_User_Risk,2)
		output.at["Expected User Risk", "USD"] = round(Expected_User_Risk,2)


	output.at["Vault USDC Holdings", "USD"] = round(T_CVOL_LP_USDC_Balance,2)
	output.at["Max Vault Risk", "USD"] = round(Max_Vault_Risk,2)
	output.at["Expected Vault Risk", "USD"] = round(Expected_Vault_Risk,2)
	
	return output
