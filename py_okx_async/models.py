from dataclasses import dataclass
from typing import Dict, Any, Optional

from pretty_utils.type_functions.classes import AutoRepr


@dataclass
class OKXCredentials:
    """
    An instance that contains OKX API key data.

    Attributes:
        api_key (str): an API key.
        secret_key (str): a secret key.
        passphrase (str): a passphrase.

    """
    api_key: str
    secret_key: str
    passphrase: str

    def completely_filled(self) -> bool:
        """
        Check if all required attributes are specified.

        Returns:
            bool: True if all required attributes are specified.

        """
        return all((self.api_key, self.secret_key, self.passphrase))


class Methods:
    """
    An instance with names of HTTP request methods.
    """
    GET = 'GET'
    POST = 'POST'


class Chains:
    """
    An instance with all chain names supported by OKX.
    """
    AELF = 'AELF'
    Acala = 'Acala'
    Algorand = 'Algorand'
    Aptos = 'Aptos'
    ArbitrumOne = 'Arbitrum One'
    ArbitrumOneBridged = 'Arbitrum One (Bridged)'
    Arweave = 'Arweave'
    Astar = 'Astar'
    AvalancheCChain = 'Avalanche C-Chain'
    AvalancheXChain = 'Avalanche X-Chain'
    BRC20 = 'BRC20'
    BSC = 'BSC'
    Bitcoin = 'Bitcoin'
    BitcoinSV = 'Bitcoin SV'
    BitcoinCash = 'BitcoinCash'
    Bytom = 'Bytom'
    CELO = 'CELO'
    CELOTOKEN = 'CELO-TOKEN'
    CFX_EVM = 'CFX_EVM'
    CORE = 'CORE'
    Cardano = 'Cardano'
    Casper = 'Casper'
    Chia = 'Chia'
    Chiliz = 'Chiliz'
    Conflux = 'Conflux'
    Cortex = 'Cortex'
    Cosmos = 'Cosmos'
    Crypto = 'Crypto'
    Decred = 'Decred'
    Dfinity = 'Dfinity'
    Digibyte = 'Digibyte'
    DigitalCash = 'Digital Cash'
    Dogecoin = 'Dogecoin'
    EOS = 'EOS'
    ERC20 = 'ERC20'
    Elrond = 'Elrond'
    Eminer = 'Eminer'
    EthereumClassic = 'Ethereum Classic'
    EthereumPoW = 'EthereumPoW'
    FEVM = 'FEVM'
    FLOW = 'FLOW'
    Fantom = 'Fantom'
    Filecoin = 'Filecoin'
    Flare = 'Flare'
    Fusion = 'Fusion'
    Harmony = 'Harmony'
    Hedera = 'Hedera'
    Horizen = 'Horizen'
    HyperCash = 'HyperCash'
    ICON = 'ICON'
    INTCHAIN = 'INTCHAIN'
    IOST = 'IOST'
    KAR = 'KAR'
    Kadena = 'Kadena'
    Khala = 'Khala'
    Klaytn = 'Klaytn'
    Kusama = 'Kusama'
    Lightning = 'Lightning'
    Linkeye = 'Linkeye'
    Lisk = 'Lisk'
    Litecoin = 'Litecoin'
    MIOTA = 'MIOTA'
    Metis = 'Metis'
    Mina = 'Mina'
    Monero = 'Monero'
    Moonbeam = 'Moonbeam'
    Moonriver = 'Moonriver'
    N3 = 'N3'
    NEAR = 'NEAR'
    NULS = 'NULS'
    Nano = 'Nano'
    NewEconomyMovement = 'New Economy Movement'
    OASYS = 'OASYS'
    OKTC = 'OKTC'
    OmegaChain = 'Omega Chain'
    Ontology = 'Ontology'
    Optimism = 'Optimism'
    PlatON = 'PlatON'
    Polkadot = 'Polkadot'
    Polygon = 'Polygon'
    PulseChain = 'PulseChain'
    Quantum = 'Quantum'
    Ravencoin = 'Ravencoin'
    Ripple = 'Ripple'
    Ronin = 'Ronin'
    SUI = 'SUI'
    Siacoin = 'Siacoin'
    Solana = 'Solana'
    StellarLumens = 'Stellar Lumens'
    StepNetwork = 'Step Network'
    TON = 'TON'
    TRC20 = 'TRC20'
    Terra = 'Terra'
    TerraClassic = 'Terra Classic'
    Tezos = 'Tezos'
    Theta = 'Theta'
    TrueChain = 'TrueChain'
    UMEE = 'UMEE'
    VSYSTEMS = 'VSYSTEMS'
    WAVES = 'WAVES'
    WGRT = 'WGRT'
    Wax = 'Wax'
    XANA = 'XANA'
    XEC = 'XEC'
    Zcash = 'Zcash'
    Zilliqa = 'Zilliqa'
    lStacks = 'l-Stacks'
    zkSyncEra = 'zkSync Era'
    zkSyncLite = 'zkSync Lite'

    all_chains = {
        'aelf': AELF,
        'acala': Acala,
        'algorand': Algorand,
        'aptos': Aptos,
        'arbitrum one': ArbitrumOne,
        'arbitrum one (bridged)': ArbitrumOneBridged,
        'arweave': Arweave,
        'astar': Astar,
        'avalanche c-chain': AvalancheCChain,
        'avalanche x-chain': AvalancheXChain,
        'brc20': BRC20,
        'bsc': BSC,
        'bitcoin': Bitcoin,
        'bitcoin sv': BitcoinSV,
        'bitcoincash': BitcoinCash,
        'bytom': Bytom,
        'celo': CELO,
        'celo-token': CELOTOKEN,
        'cfx_evm': CFX_EVM,
        'core': CORE,
        'cardano': Cardano,
        'casper': Casper,
        'chia': Chia,
        'chiliz': Chiliz,
        'conflux': Conflux,
        'cortex': Cortex,
        'cosmos': Cosmos,
        'crypto': Crypto,
        'decred': Decred,
        'dfinity': Dfinity,
        'digibyte': Digibyte,
        'digital cash': DigitalCash,
        'dogecoin': Dogecoin,
        'eos': EOS,
        'erc20': ERC20,
        'elrond': Elrond,
        'eminer': Eminer,
        'ethereum classic': EthereumClassic,
        'ethereumpow': EthereumPoW,
        'fevm': FEVM,
        'flow': FLOW,
        'fantom': Fantom,
        'filecoin': Filecoin,
        'flare': Flare,
        'fusion': Fusion,
        'harmony': Harmony,
        'hedera': Hedera,
        'horizen': Horizen,
        'hypercash': HyperCash,
        'icon': ICON,
        'intchain': INTCHAIN,
        'iost': IOST,
        'kar': KAR,
        'kadena': Kadena,
        'khala': Khala,
        'klaytn': Klaytn,
        'kusama': Kusama,
        'lightning': Lightning,
        'linkeye': Linkeye,
        'lisk': Lisk,
        'litecoin': Litecoin,
        'miota': MIOTA,
        'metis': Metis,
        'mina': Mina,
        'monero': Monero,
        'moonbeam': Moonbeam,
        'moonriver': Moonriver,
        'n3': N3,
        'near': NEAR,
        'nuls': NULS,
        'nano': Nano,
        'new economy movement': NewEconomyMovement,
        'oasys': OASYS,
        'oktc': OKTC,
        'omega chain': OmegaChain,
        'ontology': Ontology,
        'optimism': Optimism,
        'platon': PlatON,
        'polkadot': Polkadot,
        'polygon': Polygon,
        'pulsechain': PulseChain,
        'quantum': Quantum,
        'ravencoin': Ravencoin,
        'ripple': Ripple,
        'ronin': Ronin,
        'sui': SUI,
        'siacoin': Siacoin,
        'solana': Solana,
        'stellar lumens': StellarLumens,
        'step network': StepNetwork,
        'ton': TON,
        'trc20': TRC20,
        'terra': Terra,
        'terra classic': TerraClassic,
        'tezos': Tezos,
        'theta': Theta,
        'truechain': TrueChain,
        'umee': 'UMEE',
        'vsystems': VSYSTEMS,
        'waves': WAVES,
        'wgrt': WGRT,
        'wax': Wax,
        'xana': XANA,
        'xec': XEC,
        'zcash': Zcash,
        'zilliqa': Zilliqa,
        'l-stacks': lStacks,
        'zksync era': zkSyncEra,
        'zksync lite': zkSyncLite
    }

    @staticmethod
    def are_equal(chain_1: str, chain_2: str) -> bool:
        """
        Compare if the names of chains match in lowercase.

        Args:
            chain_1 (str): the first chain name.
            chain_2 (str): the second chain name.

        Returns:
            bool: True if chains are equal.

        """
        return chain_1.lower() == chain_2.lower()


class Currency(AutoRepr):
    """
    An instance of a currency.
    """

    def __init__(self, data: Dict[str, Any]) -> None:
        """
        Initialize the class.

        Args:
            data (Dict[str, Any]): the dictionary with a currency data.

        """
        self.canDep: bool = data.get('canDep')
        self.canInternal: bool = data.get('canInternal')
        self.canWd: bool = data.get('canWd')
        self.token_symbol: str = data.get('ccy')
        self.chain: str = '-'.join(data.get('chain').split('-')[1:])
        self.depQuotaFixed: Optional[str] = data.get('depQuotaFixed')
        self.depQuotaFixed = self.depQuotaFixed if self.depQuotaFixed else None
        self.depQuoteDailyLayer2: Optional[float] = data.get('depQuoteDailyLayer2')
        self.depQuoteDailyLayer2 = float(self.depQuoteDailyLayer2) if self.depQuoteDailyLayer2 else None
        self.logoLink: str = data.get('logoLink')
        self.mainNet: bool = data.get('mainNet')
        self.maxFee: float = float(data.get('maxFee'))
        self.maxFeeForCtAddr: float = float(data.get('maxFeeForCtAddr'))
        self.maxWd: float = float(data.get('maxWd'))
        self.minDep: float = float(data.get('minDep'))
        self.minDepArrivalConfirm: int = int(data.get('minDepArrivalConfirm'))
        self.minFee: float = float(data.get('minFee'))
        self.minFeeForCtAddr: float = float(data.get('minFeeForCtAddr'))
        self.minWd: float = float(data.get('minWd'))
        self.minWdUnlockConfirm: int = int(data.get('minWdUnlockConfirm'))
        self.name: str = data.get('name')
        self.needTag: bool = data.get('needTag')
        self.usedDepQuotaFixed: Optional[str] = data.get('usedDepQuotaFixed')
        self.usedDepQuotaFixed = self.usedDepQuotaFixed if self.usedDepQuotaFixed else None
        self.usedWdQuota: float = float(data.get('usedWdQuota'))
        self.wdQuota: float = float(data.get('wdQuota'))
        self.wdTickSz: int = int(data.get('wdTickSz'))


class FundingToken(AutoRepr):
    """
    An instance of a funding token.
    """

    def __init__(self, data: Dict[str, Any]) -> None:
        """
        Initialize the class.

        Args:
            data (Dict[str, Any]): the dictionary with a funding token data.

        """
        self.token_symbol: str = data.get('ccy')
        self.bal: float = float(data.get('bal'))
        self.availBal: float = float(data.get('availBal'))
        self.frozenBal: float = float(data.get('frozenBal'))


@dataclass
class WithdrawalType:
    """
    An instance of a withdrawal type.
    """
    state: str
    name: str


class WithdrawalTypes:
    """
    An instance with all withdrawal types.
    """
    Internal = WithdrawalType(state='3', name='internal')
    OnChain = WithdrawalType(state='4', name='on-chain')


@dataclass
class WithdrawalStatus:
    """
    An instance of a withdrawal status.
    """
    state: str
    name: str


class WithdrawalStatuses:
    """
    An instance with all withdrawal statuses.
    """
    Canceling = WithdrawalStatus(state='-3', name='canceling')
    Canceled = WithdrawalStatus(state='-2', name='canceled')
    Failed = WithdrawalStatus(state='-1', name='failed')
    WaitingWithdrawal = WithdrawalStatus(state='0', name='waiting withdrawal')
    Withdrawing = WithdrawalStatus(state='1', name='withdrawing')
    WithdrawSuccess = WithdrawalStatus(state='2', name='withdraw success')
    WaitingMannualReview4 = WithdrawalStatus(state='4', name='waiting mannual review')
    WaitingMannualReview5 = WithdrawalStatus(state='5', name='waiting mannual review')
    WaitingMannualReview6 = WithdrawalStatus(state='6', name='waiting mannual review')
    Approved = WithdrawalStatus(state='7', name='approved')
    WaitingMannualReview8 = WithdrawalStatus(state='8', name='waiting mannual review')
    WaitingMannualReview9 = WithdrawalStatus(state='9', name='waiting mannual review')
    WaitingTransfer = WithdrawalStatus(state='10', name='waiting transfer')
    WaitingMannualReview12 = WithdrawalStatus(state='12', name='waiting mannual review')

    statuses_dict = {
        '-3': Canceling,
        '-2': Canceled,
        '-1': Failed,
        '0': WaitingWithdrawal,
        '1': Withdrawing,
        '2': WithdrawSuccess,
        '4': WaitingMannualReview4,
        '5': WaitingMannualReview5,
        '6': WaitingMannualReview6,
        '7': Approved,
        '8': WaitingMannualReview8,
        '9': WaitingMannualReview9,
        '10': WaitingTransfer,
        '12': WaitingMannualReview12
    }


class Withdrawal(AutoRepr):
    """
    An instance of a withdrawal.
    """

    def __init__(self, data: Dict[str, Any]) -> None:
        """
        Initialize the class.

        Args:
            data (Dict[str, Any]): the dictionary with a withdrawal data.

        """
        self.chain: str = '-'.join(data.get('chain').split('-')[1:])
        self.fee: float = float(data.get('fee'))
        self.token_symbol: str = data.get('ccy')
        self.client_id: str = data.get('clientId')
        self.amount: float = float(data.get('amt'))
        self.tx_id: str = data.get('txId')
        self.from_: str = data.get('from')
        self.area_code_from: str = data.get('areaCodeFrom')
        self.to_: str = data.get('to')
        self.area_code_to: str = data.get('areaCodeTo')
        self.state: WithdrawalStatus = WithdrawalStatuses.statuses_dict[data.get('state')]
        self.timestamp: int = int(int(data.get('ts')) / 1000) if data.get('ts') else 0
        self.id: str = data.get('wdId')


class WithdrawalToken(AutoRepr):
    """
    An instance of a withdrawal token.
    """

    def __init__(self, data: Dict[str, Any]) -> None:
        """
        Initialize the class.

        Args:
            data (Dict[str, Any]): the dictionary with a withdrawal token data.

        """
        self.amt: float = float(data.get('amt'))
        self.wdId: int = int(data.get('wdId'))
        self.token_symbol: str = data.get('ccy')
        self.clientId: Optional[int] = data.get('wdId')
        self.clientId = int(self.clientId) if self.clientId else None
        self.chain: str = '-'.join(data.get('chain').split('-')[1:])
