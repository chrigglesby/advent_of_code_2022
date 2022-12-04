import string

sample_data = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

data = """BzRmmzZHzVBzgVQmZLPtqqffPqWqJmPLlL
hpvvTDcrCjhpcrvcGGhfLHMlLtMCqflNlWPJlJ
hGjhncHhGnhbTHczBBZVVSbRwgSgRV
rWVQjPQQjGRWNSrWrPjcptwBpqqJBtJBBcZgMdtq
zzmmpzfTCFpTlMlJJwBgMlqMBt
TvLszpbhhTLmsnRQPDQGWDWRvQSR
zGzvLlGlQHLGBQZlhBWhdjRdmdWRcjPj
fTJNfTfNSRWPhjdjfj
pbsbVVnpSnbVTprnbqqrzvLLgQlGLPLHll
ZCCCsWvNvmsCsCmZLZmgMLRpQMhwQRpQRfphfprpTfpM
tlncPjzlndctbzcPPBcjwDphwrfGGDffbDRpDTGG
cdqnddwzqjNVWVLZZLZq
DTLbDbRrlQbwhhNrmmfwdt
zzMJMzjCjJJjvLjMPJpcgPpzfhHdfqWcqddwtwfqdttcNtdN
pJCzVpCvDZBLsVRQ
STzBBbJzRRBZBRTqCCsfZLtNNLClCsfh
jsQnnQjjHcvQFrcPwCmtLCNlvDfftfff
sGFscMQQMMpqzqbMbd
QlNDWGsjQjgQllWQsbtzqTJczTJcbFmmFJJP
MhLrhgLVndRmzJFzVqqJqP
pSLnMdwhwdRZRSwhLZwLhdGWQjlsgWjNQWWSvgBsWDlj
THjSRFSddTjdBTcPLcVVvVBw
GzWnWfndWfznDfsnsBsPVwVwPPLL
zNflzJWqqzQDdSStHNZNpFFtbj
FSzDmsFSFlDlBzqVjqHHjHHpVgHLbp
rTrTtTQQntRQnQJQgggHZttVgHLBLhZL
WTJJRRQCRRJTRdBCRdvRNDFSWFMPmDlPPSsNPSzS
WQldlMtMVQgVMQHnDGbHGGnRnQmD
rqcZPrCFjmHlbGjZ
zSScchqwchBzTzFzhhSlcCwNtdVWWJgsVdMtWNgNVWTJTd
lMZqjMWllrTTspjprWWSSwgWNSVNDmWGVwFwgN
cdCCdLHcnndHJnmCRntLBnRzDvFNtNDVzgSgwDgFNVzFVv
BRLcCCJCmJdcRhfjPPZphrlrPqlZ
GdGqcrrZGDrvDJJqJHcBvmFFgmFMMgMgBtMLTssLmF
NbPVPDlljPmTmsTj
VfQDhflCCRWdcrQwJvvnJv
RLcWgLCqqPQLcqZwzHgwmmrmmtgwTw
DhbhNrMpnJSDJwVTHmmTVnTTVj
lrsvblMDlcWcfQPQ
PVldlphHwGwJJGdjZZWsRbbsGsNWrWQbNbQR
SqcDvTmDLtfmSmtqppfqzTgTQBrRQsbCFWbNNFQFBBrRbLNb
MgtmTgtfpqVlnVddZMwV
BdmfmPBPSbSNdGSdvWrwcZrccZPPcZnH
jzzLsjsMRlQQVHwswvvZrCHrrT
VqhzVFzplFlpLwpMphLRQQVRmSqgbdGtNJBmNSmgGbtggSgt
DHVpNZjdZjFZWVFHpvFvzmlRzPnlfznFRz
lrTBTsBwwMbrrwLPPfwGmGzvRf
scrtMhMCtJBBBclbHdHttWZWDSqDSjHj
wzqsPmqsbsfqBwPMNRMMZcZmFFNtZM
CgCnhlvvLJgcRFNNBdCpWM
QnQrVgHSvVHjbjTGBbbTHb
HdrVrdqFDdZVmHgRmDRFHMnTdTssMGnLnPJLbPTbCs
SczlScjwcNzplNzQSSfjwQSrTGGsbTsnTCnGTMCMLMGGbN
wQlfjrhfhQFHqZhRZRtD
RsfJDGJvzPNcjpddSWJWMd
LLCbBCwCrCmVVnrmhQFmbVhdcdlWpjZzSpMdWSpcWczSBj
rrLCbTwnHTvzvNGT
wPhPhbCqqSCrtJDlqvlrJr
RVVZddLFRZZcQLvJJtzptlgPJp
TVQRZGVncFdTGWZdCNShHhfPNwwsWPwb
dzLVzPSgrgDDDCMSMLLPwFmdTTcsvmwNwjNsHcFF
nWBGntQfGNGBflWBBqlpRQGbWFvjwsbsFswbvTHjjbmHTc
tBNJBnGBflQnDPJrPhDgrPVg
VtWztWtqpqzWpWzqjNRjNpWTmrrmrSbnmJwSJwnMPrCSJVwM
sDHsBDhBdsBZGcHvLHDLhhCSnRSwCJMZrPbmnMbJSCSR
ccLRhgsLBdRsdHNTFFNNgqTglqzF
hztlmDhPhgPlPNNgmZMCbmwwQjcwjjwMjVCd
RSJRrRqnqQJFqvnTGrHCcHHCCHHbHHMcMvdM
qGJsnQTRsStsftPlhPNl
BFFBLPRCwsLwhlPlRmhcGGrbmmGjfNTTnp
VJMVpzgqggJnrjmjNcMjmT
VqdSZtQgZvtdzqHqHtVZdVQpCDWWFdwlRPDpWPPBCswlWD
fCWCsjPzcbzwRSzVTzhhDLqvdg
TmJtrNJrBLSLJqgS
ptNTQFHrZlnpFPwsWMbRjCpcjR
nJmQNCmbmlllmbClbfMLjMFqbGBsdLFq
ZcgTWcTnMqqMTBqF
tPgctSnPctZZgDWzZgQHwNmHlhlmzlQhlJlw
ZpTCwpffdslvgShCBhqhRz
FDMPnNFNmBPzvRPRBg
nNgMrnnDGjDmJMmnFdZTTsdsrZrslcwcQr
pTmczpCldcdDDnPttpvWSqbpJf
jgjRZMGHhGLgQrjvPWzPJgJvzStbbq
LGNLLNBBzcDFCBwwFC
nJTTqnrNvTzNMzzNfqrTPrJnwpwPpZpsHccZVsBRpcVHwpcp
bgDhgbghLWmFmStctVpZtBCVCCpfZp
LLSgLGSjggFGbSSbmMnrvqvzjfzTNrJrqM
RRpDmmPMTjwfGmJQgQ
WsNscdnvvdVZFVnnrZbjjflwljlbzfGFjQjq
NnLZsNnrrVVVcvdBLTPCPCRMwhPMBMPhCt
lbVvzngGJnVbJHpHtHNPpdSQvc
TsMBswFZsWMWBZMNwPtNNtRNHcNpSQ
CcZCTrZDsjZTsTsshWhrWrTnfgbLDfJzVVLVVlgfnzfVGV
JzTTRtJRZWmWjrMHCT
DDFGlLGcGlSSSLsFGBspPBmNMBHMghmWNmWjWCmWtH
nSSpnbsGlLDnpPsSSspFtVvffRQdVzqvvbqdfVQwRz
sMhzszlHHDsWbthHDqsbJjpLNtmjVJmVLLVLVLBp
nrTPrGwfPLdprzJzdL
wgPQcTGGzgccwCgnRwgRChFhlWSDqWWQMWhssSsMQl
NSNmwtpSpCpvMphCsr
PHcRGPLJMrsvzsqG
QHjbnRMcfbPbQZmlZgZlgBBQ
cPRPbhQjbQRdtPQdLqLHqzFZjCFCqLjC
mmfsnnwrfvwrfSNZFzHHLDCFNlLlqDlN
wsmrwswwGTffMrBnmQttJtcMZQQtPJPbZc
MvBPDDRRdnnvHPCHZLHZsFLL
rmJcbVqbcjWwWjQHLzTZFTHSzFrpsz
cmwllVqqGJbVVVmmqbQcmgRnRvGhGfgDRDZBBBvRdd
nMvMhMnvhnbTZWSSZgHmGJDFmmNDzBmbNmdGBN
rCsPLRCssRjrLLsrLlwRVrcNJQfDQfdBmmfNBGJNzmDPfB
CRjCpLltgtJgJJWq
jshCzJpjzTPpmCWvSlpfwHfSWglf
LQMMNMnHtDtLVRvwwgRWlldgWD
qHVrQNHVMFQtrrBBQMBcrrZsZbzCZhbbJZJsmmsmFPTC
JZQZnsQNMqTngZqJBVfBfPPVBNrwvfPw
SSmDstFjpDpCszDjcLLhrPVlGlrGGVBwrvwVPt
FSssFcLjFjbmFFCzjLcFLRDnMJnTHRnZZTdWqZZWnMnRnZ
GbHRHpldwGMpWhHpCMBlCbRdVSLhnqJLSrDPLPPLPDqVDrhh
gvjWWQvgZFtQFFNqLnVnDnSJzzztDD
ZccccfTsffHdWWdRWwsw
ClCtbHMlnnPPlszV
gSDWSLgWQWQJJNWqgtQjPsnfcdVcLVdVdzfzVzff
WQgqtFQgDgQSFqJhqhSJvNDRrZMZHwHMCbZhTpZbGHMTMG
pZJZlCQtHFhPfdNfCh
zcmLSVczwcMcLDNFHdLPhPWH
szvVVnBmnTGQtHTQ
RVVCNDlNGzlGZqHGHWqWhGqQwH
ZFLFTmpLvvmSqsbb
TrfpBfJpJMlnnNfNZD
qHHlDClHhltMqQsHDhHslGznwdTnzzwDGSdfnwGnwG
mZRNcNcLLPNPBFFbbPmLmbZFSCVfJJTVndVfSwnRzznfTwCS
CcCWFbbBLCWtgWgHjghqvv
TjbzlnlFmfqCFFVVCRWr
PhMcLpPDtMLpwPDvLPJbMhSgVCGqggVqQgCqCgCgSWvv
btbZbNZhJDJJhDtwtsTTTmBzzBBmlNlmHj
FqhjWtqlqmmsnFPTCvMCQMTTCjQd
pfffRfLpgrgGgzrNVzzpGVzRCdMCPJbwwcVMbQPCJVMVdbww
DGGDZRGrHggzSsFQnnWShmtH
vtHVVMMrvVMVrSHvLgvlHcZFCnRCZcccZtRRZfJFCJ
rdDjGsdTQDcNZfdncCRR
rBDsTwBbjbmbbQswswPhqVmmSvpVhlvvqMhHhh
vGBLrqMNvqSLBvvrNbllLHfwStWWtFttccjtRtjtcj
MhCDJmhMDzmcRRcjzWfztH
ZQDmDhVVCQbBVdVNMvvv
ptCtCzhWPWptnhVzzpGZbZTjTjVjFGjVFgVl
fQswRRffmRqZlgrqqFjjSgGg
HwsQDNNsDsmRLLHmffsfvHptBnhtzCvhWpZWBdhnMdCh
RlHzzTqczBPfbnvcpB
wVtNwpSZstppwwMsZhsdnLvnbtBBmbnLFFdnmF
WNQJMVWsZWwGJWhhSNrQzlgHrDCgQRHpCHrl
RrZWpJZRrZpdTGstlchLGGlLMd
NqjDPCQPnQCSvtMzSLhhjM
nQVQDDDDfwBwNCVCNVFNpWpgJgrRTmLTmTmgRTWF
SHMcrMHpcjGcjSrMMbvSvvSvwFTLJwJNtFGFWJNtDLFTLfWN
zqRnPfzQCRzqsmRPzznhszzLtLwQwwFTgWWLDLgWFTwTNQ
qVPZmRZhsCZPhZlRCqRRRCbfpccMBjvMVjdHjjMjSvdf
VVQdHwBZLVltlddtBczhrzvGcWWFRwgsFG
TDTTTqqTSSqjqnmTmPqPPmTmGhRszvsrzsjRsccgzrRzgWGF
DpJPqpWqHbZpllpt
cCSCFsnnZFnscDtNdJFJtJtdmb
VgBqBsqRrHtNdzmNrt
BGLLVVjRBsqPBfsGwPsMfSSZCSfTZTZQpSphfS
plCHCHlgglHHGpNbtngNrDvBDpfQDBQfZDfWZVrr
mTmMLhRfwhsLPQvQZDMZQBQWMB
cwsssmqRTFFfFgtbCtGl
LQPPrCPnMZwqtRMn
cWTSlJWlcplJdDTdGdpDlGcGgqmtwwZtqRrNRRmRdNZqmgNq
GSJcJSjsjTpsvWGWBHLLvVVBBBrFrzVz
NVPCSPMNDSNFVSWCsJJJmpGmZZGLLcpZLHGGtsHt
fwzlBBqghqvzqqlDrHbpHjZHmGZbLZrHLb
dnBgnDqQvwRnSnnFMFMP
BCbPsFFwCRHmDSBmWnvDDj
phhZVzdpVfQZphhZpRhSVnjmrcvvnrWtDrvWDS
TfQJMfLphMhJdfdzpQJRTPbwHHNlgbGwsTGgCP
ttWLlnnvnNnBBtlTqWlpvpndQdZsQQFssFDdsRFdVdRNFQ
jSgrScrbGZSGrrCGsFVMssFsPPFcDDMV
bzSmJbfCZCbzLwllflwqtvvw
zmFTJwFLPmzLztmjDzTJwfNrdFNrFppBSNRGNGdbrpBR
gqlhWQgsZMsvqMlMMvsvqsNlLbcdppbrRpdbbcSrrbbr
vssCgVgCsggZQZCgsnsqWgWvfJPDLwffwTPPmzTnjTPmPmwJ
SpcRTPQLBLWpNNzjmmwwwRrR
tGlfvGhfnbDlbqlChnfFMrwsmwNssTMHMHjFwv
ZlhtCtffCdWcZWZVVT
jTTCcWHWJNgCGTzTmnzrmnGn
BwRRbFvtvvQmJJFMpMJr
ZBBwLvqbBZsRsbVsZSqbcZdJjHHjhfPCJfJfHhgc
VrnDSvvrLrfTdTLGfdRp
zcJzmcFcHGfdGmWTVd
tHsMhwPVctccHFHFcbSDbbPjnNbBnbvBQB
QttWQwLTnLnWTtnffnLQSBFVjNvBjBFNgMdCsVWsjv
pDqcmmRPHqgVBddjvN
DcclzbcbPbJLnNTfnw
plRcpsZDGlGZvWvMCNcLtttq
SrfrwSjSVrSjwbmSrHzmHJCQQPQzqttNNQJMzJtqMW
wSHVnfHfWwwHWFVfSnfgmmRsslFZZDBBGZsZsDTdGRTp
qSFQSgQNgQBrBHHcrW
VTmjVJLTwlTmwTVmsMJMVlJmPvcbvvbCBbGBPjGvBbBGWcbb
DnJTZwmnZRhnpqNdWt
dTVHjZLLZDVCfVHtLDDjQbscjWbSJMJPjsbWWb
FnqrnmzzFllmsWwtsFtQMMFc
lmqzzzngGmlNNBqGllzlBNRvptHHpTCHpDLpgDZdgvHvDD
sdRZQbCfZTSTdlfTZCffccWPHPPcPPwLwctRnLWn
BBJDzFVgCDrCJrqDJJhqJVVMLPHwcctFwcWHHGLcwGwGHnWc
ghpJgqqjCZbQdZpd
tbcpzbHSszcHBgqHGZgJJJhhww
jfvdvRTffQQrrFCRFTnGwJRqNRZVpJGZLZggLh
nQTjTnMndlTdQFMvnrClCnpzmzDtbbmBbcPSzzlmmtzP
BqBqTCSTcqHsJHHM
WWPGVPLtzVgWtjWPGzVjzVGcbDhPsRbDcsbJwNRswRDRss
VQfWjfLFGWLjdFfVzTZZpJTpnmlTrSQlBl
jLNsZjqSHCsGdsmpsm
MvnVFzWMwMVWzfnVDwfBMfnnrCtdtPmPlRrdrJCJrtPDrrPD
zznfFWwMfMfFMwVTMQFnQjhjgjSZhCNbLSTcHHgbbC
GGtssttVmvnnGNMQrrVzgwVrCWMz
FdhfhhcCDhHLfzclZMcrwcQMZM
HHqqCBhHSSpdmjGqmGjtjtjj
bbQLtGMQQtQRQtrDtGprrrbCqwplZhhqSqmdwvdzqqqhSmpS
FsJjJBfnsJcFcFfjVPjWBzldqhqnlZZZzzhmnSvSnm
JPcFfFWjFHJVVsVjPVscsDlLNRHGDbLRMRCDNrCGbG
JdMdlMRJnTwdvcjv
CDLHbNSzzLFgHvnTjrswBNBTNT
QgbvzSFQmZQPQQRW
NTBrNzrpjjjCwGbB
FRbQlcvFvcRQQlRsMlRRRZjwCqMwjmjwJZdLJmjCZC
cVPPQcvlWDNhrbPz
VdbVtbbZJdtJVVdDVZmTLqqTSQvNLjjDShhvSG
zplpnBnFpnrrlghGNpLNqHvqvjNj
cWncllnlPFWzcMwtWWtsVLVRmJWCds
ShLSTnZnTSttTSbLQdfSZTMwcDHwwcHnJvDHnlnlclMM
NmPMsssRrVwjDclHJwwR
gNNMWGzNmqGdtfZTbGGb
sWNNlRHnmJtmntJt
brbbBTbbFbCbqqGgBTrCfmQVVZfSSQQSVtJZSrVZ
bbFqvbDvvGGLGbCCtBGDLbLlcPNHhhccPNcdPPchlsdR
DCFvDvnCnNfMBmMMslDZML
SQQQJHwpSgJSJHQWSWHqJWWbmcBBBLLTsmhhTcZbMhmlshcb
RJRgpJHssgwSQHRqsQPGGjjtNCrrFvvnFjjPrP
mThmsgjzTPjMpcvtWP
GNNBVqVGNZbbNbNqqZQVNVNbWcpdtMCcpCtMWCdCPpQccmpp
VSmNrmmbBfZVlsrssrLTRhRhTn
TdmCvLDCpTRNTdFbbWnnSWCfhjbbzn
GrrMsPVGcQHBGMbhjjSgWfHHDbjb
BPBVqqrQPsQqwrrmmmJdRLDDqFRplT
fpDDJljDlCfDTjprjrfbddWthCSCtdPPQFhSSSWW
HsLZgMGbgBBsNzMvGbdVtVQzFRQSthhFPdtP
sMBmGBmbNvLHGMnrDppTcJmcjpqljf
ptSpSJQqpbNGGDDhcMWrlNHcZZWWls
zRLRRRjvvgjHMMsMpWpc
vmCPLCgwvwdnCzmvLbpTbVQqJJPbJPpTVq
TJCfhhJVFffrJJQQllNWcvWhwvWD
GPSGjjpLslBbpLpLqqqPDvdwvwvNzQWGzDDNdzGN
msbRjbpPqsRpHnlZrmJlnVHT
GGfFsCCTvGDsfTTrhsCMMzptZJMdpdgtrpdMcV
LBlwBHPSqjwwlVggHpnMZcVHMt
ZlZZlBbRPGGTGfmRsD
CtCjbVvzQQZTWVdd
MlSqWlmsmGBSHJHTDFHZ
pcqsmsplwsqclwRtRWgtRnPPvb
zCrzCrsdjrhGDCFqGDjRRPtpWfQQcpfQZcCZPp
VSVwVMgLHHLTwMDTMMVnbWPRZQRcRQPptWnpbZcb
MNBBBlSMvLVwTlVTFdNdhNhFsqsGDrzm
rBLWTwTThWwVVDTwHBsZZWppvpGtpptppmRvFFFMFMfL
qPPNCCbqcbcNqbqQjjJQqzjRpptmlpMGmMlJtftmtFHpMt
QnCgzzQbbQqPcPQnncbdQdnVTwDssZgrShBTVgZZsBSDHT
PFGJFqnfqmPgFJQPWdbLdpDRhbphWjDm
rclNHvcrzCNwrWRprjdMMMph
wsZHwZNvRRQsQqBV
LqlGCPlPLTCPqqQlpqLlWfBfWgcHNRJRfWNsncGH
VVtdwVtDDdVmhrdwSBmjbdzNHgfgJnNnsSnHsNffHgRsgR
wVzhbjmDbDrwjdbztFDDthMCvqPppZQBQLZQTqTvFTvZ
BnQnQFwRmRwmwdBSFDFnmSDVLCJTCTppVVmGLVTCLcgVpC
ZlWvhvZjNrbNvqjNhlfPfqjCGHrsspggTpVLpsJCpcJVgg
vPzNvqjWhqFzGSnRGMDG
wZnMZzzZZchDRtVsqtCtwV
WmWpWWmPPWrmrmBmWrTlTFPNVqVCRSDCQHcqVTtTqsSDSTSD
PrppdFlWWlfrWmpWFffrdcGjJJGggnnhZGdLLgGGndvz
FShHNmNhRhNJmBnQBQJrmP
VTgzDTjwfffwzDvwlcczzVSJbQlBQSWBWCnPJPbJWWbC
tzSVtzvSvGSRZqqFMNtpRR
hPZhGDZpnCGtDhznjmLmdJffdNzJ
glwsSrQwBvLdgLzdcj
QsRbHllzzlHwHlBszWlTBFbpDPMhbPDVGpGFpPtFPp
SRjStRDctgDSBzLvPvNrDhmPLr
QqTHGTPJmmHmhNmH
TGQZsTqFnQZCJTPsnJnZQMjVRBVtcVRSVRBlwccSCtBS
bbsNsvsvnNPTRRllbblLqhtQCqQSLCGGHSqHNC
wFpzFgqVzqVJWFDwqJDmSBBmHBHhShLQhCGSBCGH
MJVpFMqgwMqRRbZsMbZMrP
PPdDhvNDQdmgQPZmQVHHtHGGWVGbffWGvs
MMLCTRRLlLclTLRMRLCwMLHWVctbVVHWWWFfVjVGsFWW
MRSMMlpTJRqClBCRqBDnzqgQPnqgznZPZqbP
MrMNPNNpjvdprWtrpMsthqBfqlnfqcGhVBqFRcnqFG
QbDgSSQbgSDDmDVmlqSCRllRcFqnqfBl
QVJbVmwwDQbzVTgbppNJNMWNjNNPrdpM
WwJJNbtHfpLpVgZZPVFhZh
vmmqlDvRvRfqBSrlzmmMjRBhcVhQVZhVghCQQQQTcTrPTP
jSqMmqRzMDDjvqlBqsBMBmmwGNJwJnwLNfbGwddswnJtJH
RLgRmRggbvbzzPmmRNmzsQWFtSGNtwSNQnntFwnnCw
pDBrBHpHhlldphHBHhJVFSLnWWFJttCtQSttSS
hfHrpphHBppfTvmzgMmbLbgf"""

alpha = list(string.ascii_lowercase) + list(string.ascii_uppercase)


# Take input string, split on newline, split in half for compartments
def parse(input: str, compartments: bool):
    def compartmentalise(string: str):
        return [
            string[:len(string) // 2],
            string[len(string) // 2:],
        ]

    output = input.split('\n')
    if compartments:
        output = list(map(compartmentalise, output))
    return output


# Find dupes
# - Only lists unique dupes
def get_dupes(backpack: list):
    compartment1 = list(backpack[0])
    compartment2 = list(backpack[1])
    dupes = []

    for item in compartment1:
        if item in compartment2:
            if item not in dupes:
                dupes.append(item)

    return dupes


def backpacks_to_dupes(backpacks: list):
    return list(map(get_dupes, backpacks))


# Char to Priority value
def get_priority_value(char: str):
    if len(char) > 1:
        raise ValueError('input length exceeded 1, must be a single character')

    try:
        return alpha.index(char) + 1  # Priority value is not 0 based
    except ValueError:
        raise ValueError('unsupported character provided')


# Sum dupe values
def sum_dupes(duplicates: list):
    total = 0
    for dupes in duplicates:
        for d in dupes:
            total += get_priority_value(d)

    return total


compartmentalised_backpacks = parse(sample_data, True)
duplicates = backpacks_to_dupes(compartmentalised_backpacks)
duplicates_sum = sum_dupes(duplicates)
print(duplicates_sum)  # Answer: 7824

# Part 2


def arrange_trios(packs: list) -> list:
    trios = []
    musketeers = []

    for b in packs:
        musketeers.append(b)

        if len(musketeers) == 3:
            # Add trio
            trios.append(musketeers)
            # Reset
            musketeers = []

    return trios


# Of lists find common values, shared by all lists
def trio_to_badge(musketeers: list):
    common = []
    # Check multi list
    if len(musketeers) < 2:
        raise ValueError('expects multiple lists for comparison')

    # Loop characters of first list
    for char in list(musketeers[0]):
        is_common = True

        # Loop remaining lists
        for m in musketeers[1:]:
            # Check in this backpack
            if char not in list(m):
                is_common = False

        # Determined common and not already selected
        if is_common and char not in common:
            common.append(char)

    return common


def sum_badges(trios: list):
    badges = list(map(trio_to_badge, trios))
    total = 0

    for b in badges:
        for char in b:
            total += get_priority_value(char)

    return total


# Confirmed data set is divisible by 3
backpacks = parse(data, False)
trios = arrange_trios(backpacks)
badges_sum = sum_badges(trios)

print(badges_sum)  # Answer: 2798
