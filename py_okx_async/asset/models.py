from dataclasses import dataclass
from typing import Dict, Any, Optional

from pretty_utils.type_functions.classes import AutoRepr


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
