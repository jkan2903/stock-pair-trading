import yfinance as yf
import csv
import pandas as pd

import concurrent.futures

START = "2023-01-15"
END = "2023-02-15"

def checkTickers(symbol):
  info = None
  try:
    info = yf.Ticker(symbol).info
  except Exception:
    pass

  return (symbol, info)

def downloadData(prompt_str):
  data = yf.download(prompt_str, start=START, end=END, threads=False)
  return data

stock_symbols = "./data/nasdaq_symbols.csv"
with open(stock_symbols, "r") as f:
  reader = csv.reader(f)
  # Skip the header row (optional)
  header = next(reader)
  # Read all rows
  rows = [row for row in reader]

prompt_str = ""

info = None


# =============================================================================
#     TO BE RUN FIRST TO EXTRACT ALL STOCK TICKER VALUES THAT ARE VALID
# =============================================================================
# for row in rows:
#   try:
#     info = yf.Ticker(row[0]).info
#     if info:
#       prompt_str += row[0] + " "
#   except Exception as e:
#     # Handle cases where the ticker is outright invalid
#     print(f"Error checking ticker {row[0]}: {e}")

# with concurrent.futures.ThreadPoolExecutor() as executor:
#   futures = {executor.submit(checkTickers, row[0]): row[0] for row in rows}
#   for future in concurrent.futures.as_completed(futures):
#     symbol, info = future.result()
#     if info:
#       prompt_str += symbol + " "

# print("prompt: " + prompt_str)



sample_prompt_str = "AAPL MSFT AAL AAP ABT ACGL ADSK CENT BB BLK"

# =====================================================================================================
#     TO BE RUN NEXT (comment previous section out) TO EXTRACT ALL STOCK TICKER VALUES THAT ARE VALID
# =====================================================================================================

# split prompt_str into separate strings of tickers so that downloads can be split across multiple threads

prompt_str_1 = "A AAL AA AAON AACT AAOI AAME AAP AAPL AACG AAT AAM AADI ABAT AB ABBV ABCL ABCB ABLLL ABG ABLV ABEO ABLLW ABEV ABLVW ABL ABM ABNB ABOS ABP ABPWW ABR ABT ABSI ABVE ABVC ABTS ABUS ABR^E ABVX ABR^D AC ABR^F ACA ABVEW ACAD ACB ACDC ACCO ACCD ACEL ACGLN ACGL ACET ACHV ACGLO ACHL ACIC ACI ACIU ACHC ACIW ACLX ACHR ACM ACMR ACLS ACNB ACOG ACNT ACON ACONW ACP ACR ACN ACRS ACRV ACRE ACT ACTU ACU ACR^C ACV ACXP ADAG ACTG ACVA ACR^D ADAP ACP^A ADC ADBE ADD ADI ADIL ADGM ADM ADN ADCT ADP ADMA ADNWW ADEA ADC^A ADSK ADNT ADPT ADSE ADSEW ADTN ADT ADTX ADV ADUS AEE ADUR AEF ADX AE ADVM ADVWW AEHR AEG AEHL ADXN AEFC AEIS AEM AEMD AEO AEI AER AENTW AERT AERTW AEON AEP AESI AES AFCG AEYE AFG AEVA AFGD AFB AFGB AFBI AFGE AFL AENT AFGC AFMD AFJK AFRI AFRM AFYA AGAE AG AGCO AGEN AGD AGI AGM AGL AGFY AGIO AGNCP AGNCO AGM^G AGNC AGNCL AGM^F AGNCM AGMH AGM^D AGM^E AGNCN AGS AGO AGRI AGRO AGX AGYS AHH AHG AHCO AHL^C AHR AHT AHH^A AHL^D AI AHT^D AHL^F AHT^F AHT^G AHL^E AIG AHT^I AIFU AIEV AIFF AHT^H AIMAU AIMAW AILE AIM AILEW AIHS AIP AIMDW AIO AIOT AIR AIN AIMD AIRG AIRJW AIRS AIRE AIRJ AIRI AISP AITR AIRTP AIZ AIV AIRT AITRR AITRU AIT AISPW AIXI AJG AKA AIZN AKAM AKR AKYA AKRO AKBA AKTX AKAN ALAR ALAB ALB ALC ALCO ALDF ALBT ALCE ALDFW ALB^A ALCY ALDFU ALDX ALEX ALF ALFUW ALEC ALGM ALGN ALE ALGS ALG ALHC ALIT ALGT ALKS ALL ALK ALKT ALLO ALL^I ALLR ALLK ALL^J ALL^H ALLE ALL^B ALLY AL ALLT ALRM ALNY ALOT ALMS ALT ALRS ALRN ALSN ALTG ALTI ALTR ALTM ALTG^A ALTS ALV ALVO ALUR ALTO ALVR ALX ALVOW ALXO AM ALZN AMAT AMBC AMAL AMBA AMBI AMBP AMCR AMCX AMG AMGN AMBO AME AMC AMED AMD AMH AMLX AMLI AMIX AMKR AMH^H AMH^G AMODW AMN AMP AMPGW AMPG AMPH AMOD AMPL AMPS AMPY AMSC AMRC AMRK AMS AMRN AMR ALNT AMPX AMRX AMT AMST AMWD AMSF AMTD AMTM AMZN AMTX AMWL ANDE ANAB ANF AMX ANGH AMTB AN ANGHW ANGO ANGI ANL ANET ANG^B ANG^A ANNA ANIK ANIP ANNAW ANNX ANIX ANRO ANSC ANSCW ANSS ANTE ANTX ANY ANSCU ANVS AOMN AOS AOMR AOSL AORT AON AOUT APA AOD APCXW AP APD APAM APDN APCX APEI APG ANEB APGE API APH APLMW APLE APLM APM APLS APLD APLT APOG APO APP APOS APPF APPN APTV APRE APPS APT APTO APO^A APWC APVO APYX AQMS AQN AQB AQUNU ARAY ARBB AR AQST ARBE ARBK AQNB ARBEW ARCB ARCO ARCH ARDC ARE ARDX ARDT AREB ARCC ARBKL ARCT AREBW AREC AQU ARGD AREN ARHS ARES ARI ARGX ARKO ARKR ARKOW ARES^B ARLO ARGO^A ARIS ARLP ARL ARQ ARM ARMP ARMN AROC ARMK AROW ARQQ ARTL ARQQW ARR ARTW ARQT ARTV ARVN ARTNA AS ARW ARRY ASAI ARWR ASA ARR^C ASB ASAN ASBA ASC ASG ASGI ASGN ASB^E ASLE ASB^F ASH ASIX ASND ASML ASNS ASO ASPI ASMB ASM ASRT ASPS ASR ASPN ASPCU ASRV ASTH ASTI ASUR ASTC ASTL ASX ASTS ASYS ATAI ATCOL ASTLW ATAT ATEN ATCH ATER ASST ATEC ATCO^H ATGL ATGE ASTE ATEX ATCO^D ATHA ATHE ATH^C ATH^A ATH^D ATH^B ATI ATH^E ATKR ATHS ATHM ATLCP ATLCZ ATLC ATLO ATMV ATMCW ATMC ATLCL ATLN ATLX ATMU ATNF ATOS ATMVR ATNFW ATNI ATNM ATR ATOM ATRC ATRA ATUS ATRO ATPC ATXI ATO ATSG ATXG ATYR ATXS AU ATS AUBN AUDC AUR AUNA AUPH AUID AURA AUB AUB^A AUUD AUROW AUTL AVA AVAH AVAV AUST AVAL AVBP AVB AVGO AVD AUUDW AVDL AVGR AVK AVNW AVTE AVPT AVO AVNT AVDX AVIR AVR AVNS AVY AVT AWF AWH AWI AVXL AVTX AVTR AVPTW AWK AWR AWP AXL AWRE AXIL AXDX AWX AX AXON AXGN AXS AXTA AYRO AZEK AYTU AXP AXSM AYI AXR AZ AXTI AZPN AZO AZTA AXS^E AZI AZN AZUL AZTR BA AZZ" 

prompt_str_2 = "B BABA BAC BAC^K BAC^M BAC^B BA^A BAC^L BAC^E BAC^S BACQR BAC^P BAC^N BACK BACQ BAC^Q BAERW BAER BAFN BAH BAC^O BAK BALY BANFP BAM BAND BANR BANL BANF BANC BALL BARK BAOS BANX BANC^F BATL BATRA BASE BATRK BAX BAYAU BBCP BBAI BB BBDO BBIO BAP BBAR BBLG BBDC BBD BBLGW BBGI BBN BBW BBU BBUC BC BBWI BBSI BBVA BBY BCAB BCC BC^A BCAN BC^C BCAL BCAX BCBP BCDA BCE BC^B BCG BCGWW BCAT BCO BCRX BCOW BCML BCPC BCSF BCH BCS BCTXW BCOV BCLI BCTX BDC BDMD BCV BCYC BDMDW BDJ BCX BDL BDN BDRX BCV^A BDSX BDX BE BDTX BEATW BEAG BEAT BEAGR BEDU BEAM BECN BELFA BEKE BEEM BEN BEEP BENF BELFB BEP BEPC BENFW BEPJ BETRW BEPI BERY BEST BETR BEPH BFC BFAM BEP^A BFH BFRG BFIN BFRI BFK BFZ BFRGW BGB BFS^D BFLY BG BFRIW BFS BGH BGFV BFST BGC BGR BGSF BGI BGNE BGS BGLC BFS^E BGM BGT BHB BHAT BGX BGY BHC BH BHFAM BHF BHE BHFAL BHFAN BHFAO BHIL BHFAP BHK BHP BHM BHR BHR^B BIAFW BIAF BIDU BHLB BHR^D BIGC BHVN BIIB BHST BHRB BHV BIO BIOA BIOX BIPC BILI BIP BIP^A BIGZ BILL BIP^B BIPI BITF BIT BIPJ BIRK BIPH BIRD BJRI BJ BIVI BKNG BJDX BKH BKE BK BKKT BKR BKHA BKSY BKD BKN BKHAR BKYI BKT BLAC BLBD BLACR BKTI BKV BLBX BLDE BKU BLD BL BLCO BLDEW BLE BLFY BLDP BLFS BLKB BLK BLND BLIN BLDR BLNK BLMN BLMZ BLTE BLW BLRX BLUE BMBL BLX BME BLZE BMEA BMA BMRA BML^J BMO BMRC BML^G BML^H BMI BMEZ BMN BMRN BMR BMTX BML^L BMY BNIX BNAI BNGO BNH BNED BNR BNJ BNAIW BNL BNIXW BN BNIXR BNS BNTC BOC BNRG BODI BNT BNY BNZIW BOE BOF BNZI BOH BNTX BOLT BOLD BOKF BOOM BOSC BORR BON BOOT BOW BOXL BOH^B BOWNU BOWN BOH^A BPOP BOX BP BOTJ BPOPM BPMC BPT BPRN BPTH BR BRACR BPYPM BPYPO BRAG BPYPP BRC BRAC BQ BRBR BRCC BPYPN BRIA BRFH BRBS BRID BREA BRDG BRKL BRLS BRLT BRFS BRKR BRLSW BRN BRNS BRSP BRO BROS BRT BROG BRW BSBK BRZE BSBR BRX BRTX BRY BSET BSAC BSLK BSGM BSIG BSL BSRR BSM BSLKW BST BSVN BSTZ BSX BSII BTBD BTA BSY BTBT BTCM BTG BTAI BTCTW BTDR BTBDW BTCS BTE BTCT BTMWW BTOC BTI BTOG BTM BTSG BTT BTMD BTZ BTSGU BTTR BTO BUJAR BUJAW BUR BUSE BURL BVFL BV BTU BUI BUD BVN BW BWAY BWA BWBBP BVS BWB BURU BWLP BWG BWIN BWEN BWMN BWNB BWSN BW^A BX BXC BWFG BWXT BXP BWMX BXMX BXMT BXSL BYNO BYD BY BYM BYFC BYSI BYND BZFD BYON BZFDW BYRN BZH BZUN BZ"

prompt_str_3 = "C CABA CAAS CAAP CACC CABO CAC CAKE C^N CAG CAH CAL CAF CAE CALC CADL CACI CADE CADE^A CALM CALX CAMP CAPN CAMT CAPNU CAPL CANG CAPTW CAN CAPT CARG CARA CAR CARE CANF CARM CARR CARS CAPR CASK CARV CATO CASI CASS CART CASY CATX CATY CB CAVA CBLL CBAT CBL CBNK CBNA CAT CBAN CBFV CBOE CBU CASH CBZ CBT CC CBRE CBUS CBSH CBRL CCCS CCBG CCG CCAP CCCC CCEP CCEC CCD CCIA CCB CCEL CCIR CCGWW CCIRU CCIF CCI CCIRW CCIXW CCIX CCJ CCL CCK CCIXU CCNE CCLD CCM CCLDP CCRN CCRD CCNEP CCO CCS CCSI CCOI CCLDO CCTG CDE CDLR CCZ CCU CDMO CDNA CDIO CDLX CDP CDIOW CDNS CDT CDRO CDRE CDR^C CDTX CDR^B CDTG CDTTW CDROW CDXC CDW CDZI CEAD CEADW CE CDZIP CDXS CECO CELU CEE CELC CELH CENTA CENX CENN CEIX CELUW CELZ CEG CENT CERS CEP CERO CEPU CERT CEV CETY CET CEROW CFB CETX CF CEVA CFFI CFFN CFLT CFBK CFG CFR CG CGBD CGBDL CFG^H CGAU CGBSW CGABL CGBS CFSB CGEM CFR^B CGC CGEN CFG^E CGON CGO CGNX CGTX CGNT CHCO CGTL CHCI CHD CHCT CHE CHAR CHGG CHH CHDN CHEF CHEK CHKP CHI CHMG CHEB CHPT CHNR CHMI CHN CHRS CHRD CHSCL CHMI^B CHSCN CHMI^A CHR CHSCO CHRW CHRO CHSCP CHSCM CHW CHX CHT CHTR CIB CHSN CHWY CICB CIEN CHY CIA CIFR CI CIF CIFRW CIK CII CIG CIGI CIM CINT CIMN CINF CIM^A CIO CIMO CINGW CIM^B CIM^C CING CITEW CISO CITE CION CISS CIM^D CIVB CIVI CKX CKPT CJET CIO^A CLAR CLBT CLBR CL CJJD CLB CLCO CIX CLBK CLF CLGN CLDX CLH CLEU CLDT CLFD CLIK CLDI CLM CLMB CLNN CLMT CLLS CLDT^A CLNE CLPS CLIR CLPR CLPT CLNNW CLOV CLSK CLRB CLS CLSKW CLVT CLSD CLRC CLW CLWT CLST CLYM CLRO CMBM CMCM CMA CM CMCL CMBT CLX CMC CMG CMCO CMCSA CME CMI CMND CMLS CMCT CMPO CMPOW CMP CMMB CMPX CMPS CMRE CMPR CMSD CMSC CMRX CMS CMSA CMRE^B CMT CMS^C CMRE^D CMU CNC CNA CMRE^C CMS^B CMTL CNCK CNCKW CNDT CMTG CNET CNEY CNH CNFR CNF CNMD CNL CNK CNI CNO CNNE CNM CNQ CNTA CNS CNSP CNP CNSL CNOBP CNTM CNTY CNTX CNOB CNX CNO^A CNXC CNXN CNTB COCH COCO CODA COCP CODI COE COCHW CODX CODI^A CNVS CODI^C COF COEP COEPW COF^J CODI^B COF^I COFS COGT COF^K COF^L COKE COHN COLD COIN COHR COHU COLB COF^N COLM COMM CON COOK COOP CORZ COOT COO COP COLL CORT CORZW COMP CORZZ COOTW COSM COR COTY COYA COST CP CPAY CPB COUR CPAC CPA CPF CPHC CPBI CPNG CPHI CPIX CPRI CPK CPS CPSS CPRT CPOP CPRX CPTN CPTNW CPSH CR CRAI CPT CRBD CQP CPZ CRBP CRCT CRDF CRC CRDL CRDO CRESW CREG CRBU CRBG CRESY CREV CREVW CREX CRF CRH CRGY CRGOW CRGO CRI CRIS CRM CRKN CRGX CRML CRMD CRK CRL CRMLW CRNC CRSP CRS CROX CRON CRMT CRSR CRT CRTO CRNT CRNX CRVS CRUS CRWS CRVL CSCI CRWD CSGP CSBR CRVO CSAN CSCO CSGS CSLM CSL CSLR CSLRW CSQ CSIQ CSPI CSR CSTE CSTL CSV CSX CSTM CSWC CSWI CSWCZ CTAS CTCX CTCXW CTA^A CTA^B CTKB CTBI CTBB CTHR CTGO CTM CTLP CTDD CTOS CTNT CTMX CTNM CTO^A CTOR CTRM CTRE CTRI CTS CTRA CTO CTSH CTV CTSO CUBA CTRN CTXR CTVA CUB CUBB CUBWU CUE CUBWW CUBI CUK CURB CURI CURIW CUBE CURR CUBI^F CULP CVAC CVE CURV CVCO CVEO CUBI^E CVBF CUZ CVGW CVI CUTR CVM CVR CVLG CVNA CVGI CVKD CVRX CVV CWBC CWEN CVLT CW CWAN CWK CWH CWCO CWD CVS CVX CVU CXH CXM CX CWST CXAI CWT CXT CXDO CXE CYBN CXAIW CYBR CYCN CXW CYTH CYD CYRX CYH CYN CYTHW CYTK CZNC CZR CZWI D CYCC CZFS DAC DAKT DAIO DAN DADA DAL DAR DALN DATS DASH DAVA DAVEW DATSW DAO DAWN DAY DBD DARE DBI DAVE DBL DB DBRG DCBO DBVT DC DCOM DBRG^H DCGO DCO DBRG^I DBRG^J DCOMG DCOMP DBX DCTH DDI DDL DDC DDD DDOG DD DDS DDT DCI DE DEC DECA DECAW DEA DEI DEVS DELL DEO DENN DERM DESP DFH DFIN DECK DFLIW DFLI DFS DGII DGHI DG DFP DGX DGICA DGICB DHC DGLY DHAIW DHF DHAI DHCNL DHT DHY DHI DH DIBS DIAX DHX DHCNI DHR DHIL DIOD DIN DIST DINO DIS DJTWW DIT DJCO DJT DLB DLHC DK DKNG DKL DLPN DLNG DKS DLO DLR DLTH DLX DLTR DLY DM DLNG^B DLR^L DLNG^A DMA DLR^K DMAC DMN DMYY DMLP DMB DMRC DNB DMO DNLI DNA DNMR DLR^J DOC DNN DNUT DNOW DOCS DOMH DOLE DNP DOGZ DNTH DORM DOCN DOUG DMF DOX DOV DOYU DOMO DOOO DPG DQ DOW DOCU DRDBU DPZ DPRO DRH DRI DRRX DRMA DRCT DRS DRD DRIO DRTS DRMAW DRTSW DSGN DRUG DRVN DSGX DSS DSP DSGR DSU DSL DRH^A DSM DT DSWL DSX DSYWW DSY DTB DTE DTC DTCK DSX^B DTIL DTG DTF DTI DTSQ DTSS DTM DTSTW DTST DTW DUK DTSQR DUO DUOT DV DVA DUKB DUOL DVN DX DWTX DUK^A DWSN DXLG DVAX DXPE DXC DXCM DXR DYCQR DYAI DYCQ DXYZ DX^C DY DYN DYNXU"

prompt_str_4 = "E EA EAD EARN EAT EAI EAF EBAY EB EAST DYNXW EBC EBS DYNX EBTC ECAT EBR ECC EBON EC EBF EBMT ECCV ECBK ECCC ECCF ECDA ECCU ECCW ECOR ECG ECO ECCX ECC^D ECPG ECF ECF^A ECVT ECXWW ECX EDBL ED ECL EDBLW EDIT EDRY EDF EDAP EDN EDD EDR EDUC EDU EDTK EEIQ EEFT EEA EFC EE EEX EFOI EDSA EFC^B EFC^C EFR EFSCP EFC^D EFT EFXT EFC^A EFX EFSH EG EGAN EGY EGBN EHC EFSC EICA EHAB EHTH EHGO EICC EHI EICB EIIA EIC EIM EIG EIX EL EKSO ELA ELAB EH ELAN ELC ELEV ELF ELBM EJH ELMD ELDN ELLO ELME ELP ELSE ELUT ELV ELS ELTK ELVA ELTX ELPW ELVN ELPC EMCG EMCGW ELWS EM EME EMF EMBC EMD EML EMN EMP EMKR ENGN EMR ENFN ENGNW ENB ENIC ENJ EMO EMX ENFY ENR ENS ENO ENLV ENOV ENLT ENSC ENLC ENTA ENSG ENPH ENTO ENZ ENTX ENTG ENVX EOD ENX ENVA ENVB EOSEW EOI EOLS EOS EOSE EONR EOG EP EPAC EOT EP^C EPR EPC EPM EPOW EPIX EPD EPSN EPRX EPAM EQ EQC EQH EQBK EPRT EPR^C EPR^E EQNR EPR^G EQV EQR EQIX EQH^A EQH^C ERC EQT ERH EQS ERAS ERIC ERJ ERII EQX ERNA ERO ERIE ES ESAB ESE ESGR ESCA ESGRO ESGL ESI ESEA ESHA ESGRP ESHAR ESLA ESGLW ESOA ESPR ESQ ESNT ESRT ESS ESP ESLT ESSA ET ESTA ESTC ETG ETD ETB ETJ ETN ET^I ETON ETI^ ETNB ETWO ETO ETR ETY ETSY ETW EUDA ETX EUDAW EU EURK EVC EURKR EVBN EVAX EVER EVEX EVGN EVGOW EVLV EVGR EVCM ETV EVH EVI EVLVW EVGO EVF EVR EVO EVG EVOK EVTC EVTL EVTV EVM EVT EVN EVV EWCZ EW EWTX EVRG EXEEL EWBC EXC EXEL EXAS EXE EXG EXFY EXK EXOD EXPD EXPE EXPI EXPO EXTR EXP EVRI EYE EXR EXTO EZPW EYPT EYEN EXLS F EZGO EZFL FAAS FA FAASW FACTW F^C F^B FAMI FACT FARO F^D FARM FAF FANG FAT FATBB FAST FBIO FBIOP FATBP FAX FBIN FBLA FATBW FBK FBLG FBIZ FBRT FBMS FBP FATE FBNC FBYDW FCAP FBRX FC FBYD FCFS FCEL FCCO FCBC FCF FCNCP FCNCA FCNCO FCO FCT FCUV FDMT FDBC FBRT^E FDSB FCN FCRX FDP FDUS FCPT FCX FDX FDS FEDU FEAM FENG FE FEMY FEBO FEIM FF FERG FENC FELE FFBC FET FER FFA FFIEW FFC FFIC FFIE FFNW FGEN FGBI FGB FGF FFIN FGBIP FGIWW FGFPP FGI FFIV FGL FGN FHI FG FHB FFWM FHTX FI FIGS FINS FHN^B FHN^E FHN^F FICO FIHL FIBK FHN FHN^C FINV FIP FISI FITBO FIVE FIS FITBP FITBI FIX FIZZ FKWL FITB FL FIVN FLG FLEX FINW FLGT FLL FLC FLGC FLNG FLG^A FLNT FLO FLR FLIC FLG^U FLS FLUT FLNC FLWS FLUX FLX FLYX FLXS FLYW FMAO FLYE FMN FMNB FMBH FMS FMST FN FMC FMSTW FNA FMY FMX FND FNF FNKO FNGR FNWD FNLC FNWB FOA FNB FOF FOLD FONR FOR FORD FORLW FOSL FNV FORA FORR FORL FORTY FOSLL FORM FOX FOUR FOXA FPAY FOXX FOXO FOXF FPF FOXXW FPH FRA FPI FR FRD FRBA FREY FRO FRGT FRME FRMEP FRGE FRPT FRPH FRHC FRST FROG FRSH FRT FSBW FRSX FRAF FSHP FSCO FSFG FSEA FSLR FSI FSK FSBC FSTR FSS FSP FSLY FT FTAI FSV FRT^C FTAIM FSUN FTAIN FTAIO FSM FTDR FTFT FTCI FTEL FTHY FTEK FTIIU FTII FTHM FTLF FTRE FTF FTV FUFU FTS FTI FTNT FUBO FUL FUFUW FTK FULTP FULC FUNC FUSB FUN FVN FVNNR FVCB FUND FULT FUTU FVRR FURY FVR FXNC FYBR FWRD FWRG G FWONK GABC GAIN GAINI FWONA GAIA GAB GAINZ GAB^G GALT GAINN GAINL GAMB GAB^K GAME GAM GAN GAB^H GASS GATE GAP GAU GATEW GATO GB GANX GBAB GBBK GBBKR GBBKW GAM^B GBCI GBDC GBR GBLI GBIO GBX GCI GCMG GCO GCMGW GBTG GCTK GCTS GCT GDC GDEN GDDY GDEV GATX GDL GCBC GDHG GAUZ GD GCV GDO GDS GDRX GDV GDTC GDOT GDL^C GE GEAR GDYN GECC GDV^H GDV^K GECCI GECCZ GECCH GECCO GEGGL GEG GEHC GEF GENK GEL GENC GEOS GENI GEN GERN GEO GELS GETY GES GF GEV GFI GGAL GFL GEVO GGB GFAIW GFF GFAI GFR GFS GGG GGN GGZ GHC GHG GH GGT GGR GHLD GGROW GGT^E GGN^B GGT^G GHM GHRS GHI GIB GIFI GHY GIG GIGGW GIFT GIGM GIC GILT GIPR GILD GIII GIPRW GITS GIS GJH GJO GJS GJP GIL GLBZ GL GLAD GLADZ GKOS GLBS GLBE GJT GL^D GLE GLNG GLDD GLMD GLOB GLDG GLRE GLQ GLP GLSI GLOP^A GLPI GLOP^C GLOP^B GLPG GLO GLST GLSTR GLSTW GLUE GLV GLTO GLYC GM GLW GLXG GLU GLP^B GME GMED GLU^A GMAB GMRE GNE GMM GMGI GLU^B GNL GMS GNK GNFT GNLN GMRE^A GNL^A GNRC GNS GNLX GNL^B GNL^D GNT GNPX GNL^E GNTX GNW GNTA GNTY GODN GOCO GNSS GO GOEVW GOEV GNT^A GOGO GOF GOLF GOGL GODNR GOOD GOLD GOOS GOOGL GOODN GORO GOTU GOSS GOODO GOOG GOVX GOVXW GPC GPI GPATU GORV GPJA GPMT GPAT GPN GPK GP GRABW GPRK GPRE GRAB GPMT^A GRAF GPCR GPRO GPUS GPOR GRAL GRBK GRFS GREEL GRF GRC GRCE GRFX GREE GRDN GRBK^A GRMN GRI GROV GRNQ GRO GRNT GRND GRPN GRRR GRX GS GROY GROW GRWG GRVY GSBC GRRRW GSAT GRYP GS^D GSK GSIT GS^A GSHD GSBD GS^C GSIW GSM GSMGW GSL GSRTR GSRTU GTBP GT GSUN GSRT GTES GTI GTEC GTIM GTE GSL^B GTN GTLB GTX GTLS GUG GTY GUTS GVH GURE GVA GUT GWAV GTLS^B GWH GV GWRS GWW GXAI GYRO HAE GXO H GUT^C GWRE HAFC GYRE"

prompt_str_5 = "HAFN HAIN HAL HASI HALO HBAN HAYW HBANL HBANP HAO HBANM HAS HBCP HBIO HBB HBNC HCC HCI HBI HBT HBM HCA HCAT HCKT HCM HCP HCSG HCTI HD HDB HCWC HDL HCWB HCXY HDSN HEES HE HEPS HEAR HEQ HELE HEPA HFBL HFRO HFFG HESM HEI HES HGLB HG HHH HFWA HGBL HGTY HGV HI HHS HIHO HIFS HFRO^A HIO HIT HIMX HIMS HIPO HII HIG^G HIW HIVE HITI HKIT HLF HIX HL HIG HLIO HLI HLT HLN HLNE HLIT HKD HLLY HLP HLVX HLXB HL^B HLX HMN HNI HNNA HNST HNRG HLMN HMC HMY HNVR HNW HNNAZ HOLOW HOFT HON HOFVW HOFV HMST HOLX HOG HOMB HOLO HOND HONDU HONE HOOD HOTH HONDW HOVNP HOOK HOUR HOUS HOVRW HOV HOVR HOPE HPF HP HPAI HPI HPAIW HPH HOWL HPK HPP HPKEW HPE HQY HPE^C HR HPQ HQH HQI HPS HRL HQL HRMY HROWM HRB HPP^C HRTX HRTG HRZN HROW HSBC HROWL HRI HSCS HSAI HSDT HSCSW HSII HSPOU HSIC HSPOW HSPO HSON HSHP HST HSTM HSY HTCO HTCR HSPOR HTD HTFC HTGC HTFB HSPTU HTBK HTBI HTIBP HTHT HTLF HTOO HTLFP HTLD HTZWW HTIA HTLM HTH HTZ HUBC HUBCW HUBB HUBG HUBS HUDI HTOOW HUMA HUHU HUM HUMAW HUIZ HUBCZ HUSA HURN HUN HUT HURA HURC HUYA HVT HWBK HWCPZ HWKN HWM HWH HWC HYFM HXL HY HYI HYB HYAC HYLN HYMCW HWM^ HYMCL HYPR HYMC HYZN HYT IAC HZO IAF HYZNW IAE IART IAS IAUX IBAC IBCP IBEX IBIO IAG IBN IBKR IBTA IBP IBM IBG IBTX IBOC ICCC IBO IBRX ICAD ICCH ICHR ICL ICCT ICE ICFI ICG ICON ICLR ICLK ICU ICUCW ICMB IDA ICCM ICUI ICR^A IDE IDR IDN IE IDYA IDT IDCC IEX IESC IDAI IEP IFF IDXX IFBD IFRX IGC IGA IFS IH IGT IGR IGIC IGI IGMS IGD IFN IHRT IHG IHS IIIN IHD IIF IHT IINNW III IIM IINN IIIV IKT IKNA IIPR ILLR ILAG ILLRW ILPT IMAB IMMX IMCR IMMR IMKTA IMAX IMMP IMG IMNN IMCC IMNM ILMN IMRX IMPPP IMPP IMOS IIPR^A IMTX IMO IMRN IMTE IMVT IMTXW IMXI INBKZ INAB INBX INBK INBS INCR INDI INDO INDP INCY INDB IMUX INFN INFU INDV ING INFA INGM INGN INFY INGR INLX INM INHD INMD INKT INN INOD INO INMB INSE INNV INN^E INSW INSM INSP INN^F INSI INSG INTA INTJ INTC INTZ INTR INUV INTG INTT INVA INTS INVE INV INTU INVZW INZY IOBT INVX INVZ INVH IONS IOSP IOR IONR IOVA IPA IPAR IP IONQ IPDN IPGP IOT IPI IPHA IPG IPWR IPXX IPSC IPXXU IPW IQI IPX IPXXW IRBT IQV IRD IREN IRIX IRDM IQ IROH IR IRMD IRM IRS IRON IRTC IRWD IROQ ISD IRT ISPOW ISPC ISPR ISDR ISPO ISRLW ISRG ISRL ISTR IT ISSC ISRLU ITIC ITGR ITOS ITCI ITRG ITRM ITP ITRI ITUB ITT ITW IVAC ITRN IVDA IVA IVP IVCA IVDAW IVR IX IVVD IVZ IXHL IVT IZTC IZEA JACK IVR^C IVR^B JAKK J JAMF JAGX JANX JBL JBHT JAZZ JBI JBLU JBDI JBSS JBT JCI JCE JCTC JCSE JEQ JEF JD JFBR JELD JDZG JFIN JFR JFBRW JHI JHX JHS JFU IZM JGH JHG JG JKHY JILL JJSF JL JLL JLS JMSB JMIA JMM JOB JNJ JOBY JOF JPC JNPR JNVR JOE JOUT JPI JKS JRS JBGS JRI JPM JPM^M JPM^D JPM^L JRVR JRSH JPM^C JPM^J JSPRW JTAI JSPR JSM JWEL JUNS JWN JVA JXG JVSA JXN JQC JUNE JZ JPM^K JYD KALA JXN^A KALV KAPA KAR KAI KALU KAVL JYNT JZXN KARO K KBH KBR KC KDLY KDP KBDC KELYA KDLYW KB KEP KEN KD KEQU KELYB KEY KE KEX KEY^K KFRC KFFB KEYS KEY^J KGC KFY KEY^I KFS KHC KGEI KIM KF KIND KIDS KEY^L KGS KINS KIM^N KITTW KKRS KIO KIM^M KIRK KITT KIM^L KLIC KLTO KLTR KLAC KMB KLXE KMI KKR KLG KMDA KLC KLTOW KMPR KMT KN KMX KNOP KNDI KMPB KNSL KNW KNSA KNF KOF KNTK KO KODK KOD KNX KOP KORE KOS KOPN KPTI KPLT KPLTW KPRX KR KOSS KRC KRG KRMD KREF KRKR KREF^A KROS KRNT KRO KRUS KRNY KRRO KRON KRYS KSPI KRP KTB KT KSS KTN KSCP KTCC KTH KTF KTTA KTOS KVACW KVUE KVAC KUKE KTTAW KULR KVHI KRT KWE KVYO KURA KW KWESW KYMR KWR KZIA KZR KXIN KYTX KYN"

prompt_str_6 = "L LAB LAAC LAC LAD LAES LAKE LADR LAMR LARK LANDO LANV LANC LANDM LAND LASE LANDP LATG LAUR LATGU LASR LAZR LBRDK LBRDA LAZ LAW LBRDP LBTYA LBGJ LB LBRT LBTYB LBTYK LCID LCFYW LCFY LC LCII LCUT LCTX LDI LCNB LDOS LDP LDTCW LDTC LDWY LEA LE LEDS LEE LEGT LECO LEG LENZ LEGN LEN LEGH LEU LEO LESL LEVI LFCR LFLY LEXX LFLYW LFMD LEXXW LFMDP LFST LFUS LFWD LFVN LGCB LGHLW LGCY LFT^A LFT LGHL LGL LGMK LGND LGI LGIH LGCL LGO LGVN LH LHX LI LGTY LICN LICY LIEN LIF LII LILAK LINC LILA LINK LIDR LIND LINE LIN LIDRW LIPO LIQT LION LITE LITM LIVE LIXTW LIVN LITB LKCO LKFN LKQ LLYVK LIXT LMAT LMB LLY LMFA LMND LLYVA LMT LMNR LNN LNKB LNC LNG LNT LNSR LNKS LNC^D LND LNZA LNTH LNW LOCL LOCO LOAR LOBO LOAN LODE LOB LOGC LOMA LOOP LNZAW LOPE LOTWW LPA LOW LOGI LOT LPAA LOVE LPBB LPAAW LPAAU LPLA LPBBW LPBBU LPCN LPRO LPL LPG LPSN LQDA LPTX LPTH LPX LRN LRFC LSAK LRHC LQDT LRE LRMR LRCX LSB LSBK LSE LSBPW LSEAW LSF LSEA LSCC LSTR LSPD LTC LSTA LTM LTBR LTH LSH LTRN LTRX LTRY LUCK LU LTRYW LUCY LUCD LUMN LUCYW LULU LUNR LUNA LUNG LUXH LUNRW LUXHP LVLU LVO LVROW LUV LVS LVTX LW LVWR LWLG LWAY LX LVRO LXEO LXFR LXP LXEH LXU LXRX LXP^C LYV LYT LYB LYRA LYG LYFT LZ LYEL LYTS LZB M LZM MACI MAGN MAIA MAG MACIW MAC MAA MACIU MA MAA^I MAMA MAIN MAMO MANH MAPS MAN MANU MARPS MAR MARXR MAPSW MARA MARX MAT MASS MARXU MATH MATX MASI MATV MAV MATW MAS MAYS MBAVU MBIN MBC MAXN MBAV MBCN MAX MBI MBINL MBINN MBNKP MBLY MBINO MBOT MBRX MBINM MBUU MBX MCB MBIO MBWM MCD MCHP MCBS MCFT MCHX MCI MC MCK MCN MCR MCVT MCY MCRI MCS MCW MDAI MCO MDAIW MDB MCRB MD MDBH MDCXW MDIA MDRRP MDLZ MDCX MDU MDT MDGL MDV MDRR MDWD MDXH MDXG MEGI MEGL MEDP MED MEI ME MDV^A MEG MEC MELI MEOH MESA MEIP MESO MET META METC METCB MERC MET^F MET^A METCL MER^K METCZ MFA MET^E MFC MFAO MFAN MFH MFG MFIC MFIN MFA^B MFICL MFA^C MFM MGA MGEE MFI MGF MGLD MGIC MGIH MGM MGNX MG MGNI MGR MGPI MGRE MGRB MGRC MGRD MGRM MGRX MGOL MGYR MGX MGTX MGY MHD MHK MHI MHLA MHH MHF MHNC MHUA MHLD MHO MI MHN MIND MIO MIN MIR MIDD MIGI MIRA MITK MIRM MIST MITAU MITA MITP MITT MITN MITQ MKDWW MKC MITT^B MITT^A MIY MKFG MKDW MKTW MKTX MKSI MKL MITT^C MLCO MLACU MLEC MLECW ML MLGO MLM MLNK MLKN MLI MLP MLR MKZR MLTX MLSS MLYS MMD MMLP MMC MMT MMA MMU MMSI MMI MMVWW MMM MMS MMV MLAB MNDO MMYT MNPR MNOV MNKD MNDY MNRO MNMD MNSB MNSBP MNDR MNR MNTS MNST MNSO MNTK MNTSW MNTX MNY MOB MO MNYWW MOBBW MOBX MOD MODD MODG MOBXW MOFG MOH MODV MOGO MOGU MORN MOS MOLN MOVE MOMO MOV MPA MPAA MPB MP MPC MPLN MPTI MPU MPV MPW MPLX MQ MQT MQY MPX MRBK MPWR MRCC MRC MRAM MREO MRKR MRCY MRNA MRIN MRK MRM MRNOW MRNS MRT MRSN MRNO MRTN MRVI MRUS MRVL MRX MS MS^K MS^A MS^E MS^L MS^I MSA MS^F MSAI MS^P MSAIW MS^O MSBI MSB MSCI MSBIP MSDL MSC MSD MS^Q MSEX MSGE MSGM MSFT MSPR MSS MSPRZ MSM MSI MSPRW MSN MSTR MSSAW MSGS MSSA MSW MTB MTA MTAL MT MTCH MTC MTD MTB^H MTEX MTB^J MTG MTEK MTH MTEN MTLS MTDR MTN MTEKW MTR MTNB MTRX MTVA MTUS MTX MTRN MTSI MTTR MU MUC MUA MTW MUE MTZ MUJ MUFG MUR MURA MULN MUX MVF MUSA MVBF MVO MVST MVIS MVSTW MUI MVT MX MXE MXF MXC MWA MXL MYD MWG MXCT MYGN MYFW MYE MYND MYN MYNA MYO MYI MYPS MYPSW MYSZ MYTE MYNZ NABL NAD NAK NA NAN NAMS NAAS MYRG" 

prompt_str_7 = "NAC NARI NAOV NAMSW NAII NAUT NAYA NATH NATR NAMI NAT NAVI NATL NB NBBK NBB NAZ NBHC NBIS NBIX NBN NBTB NBH NBR NBTX NBXG NBY NC NCA NCDL NCI NCL NCEW NCLH NCNO NCNA NCMI NCPL NCPLW NCRA NCSM NCV NCTY NCZ NDAQ NDMO NDRA NDLS NCV^A NECB NE NEE NCZ^A NEA NDSN NEGG NEE^N NEOG NEHC NEM NEHCW NEO NEE^S NEN NEE^R NEE^T NEON NEOV NEP NERV NET NESRW NEPH NETD NEUE NEOVW NETDW NEU NEWT NESR NEWP NEWTG NEWTZ NEWTH NEWTI NEUP NEXA NEXN NFBK NFE NEXT NFG NFGC NG NGG NFJ NFLX NGL NGVT NGNE NGVC NGS NGD NGL^B NHI NHC NGL^C NHS NHTC NICE NIC NIM NINE NI NIOBW NIPG NITO NIE NIU NIO NIVF NISN NIVFW NJR NKE NKGN NKTR NKLA NKTX NIXX NKGNW NKX NKSH NL NLY NLSPW NLOP NMAI NLSP NMFC NMCO NMHI NMG NLY^G NMI NLY^F NMHIW NMFCZ NML NMIH NMM NLY^I NMRA NMRK NN NMT NMZ NMS NNAVW NMR NNE NNBR NNN NMTC NNI NNY NOA NNVC NNDM NNOX NOC NODK NOAH NOM NOMD NOG NOEMU NOTV NOTE NOK NOV NOW NOVA NPCE NOVT NPKI NPCT NPFD NPV NPO NQP NRDS NRDY NPK NREF NPWR NRC NRGV NRIX NRIM NRG NRO NRSN NRSNW NRK NRP NREF^A NRUC NRXS NRXPW NRXP NSA NRT NSYS NSTS NSC NSPR NSSC NSIT NTB NSP NTAP NTCL NSA^A NTGR NTIP NTCT NTIC NSA^B NTES NTLA NTRB NTR NTNX NTRBW NTRS NTST NTRSO NTWK NTZ NTRA NTRP NTWOU NUE NUKK NU NURO NUWE NUKKW NUS NUVB NUVL NUV NVA NVACR NUW NUTX NVCT NVAWW NVCR NVEC NVDA NVAX NVACW NVG NVFY NVEE NVGS NVMI NVNIW NVO NVNO NVNI NVRI NVRO NVST NVTS NVR NVT NVS NVX NVVE NWBI NVVEW NWE NWGL NWL NWFL NWPX NWN NWS NWSA NWG NWTNW NX NWTN NXC NXDT NXGL NXG NXGLW NXE NXN NXJ NXP NXLIW NXPI NXDT^A NXL NXTT NXT NXPLW NXPL NXTC NXRT NYAX NYMTI NYC NYMT NXST NXU NYMTM NYMTL NYMTN NYMTZ NYXH NYT NZF OACCW OABI OACCU O OACC OAKUW OAKU OB OBDC OAK^B OBT OBDE OBLG OBK OAK^A OBIO OC OBE OCC OCCI OCCIM OCCIN OCEA OCFCP OCFT OCG OCCIO OCFC OCGN OCS OCEAW OCSAW OCSL OCTO OCUL ODC ODP OESX OEC OCX OFG ODD OFLX ODFL OFS OFSSH OFIX OGE OGN OGI ODV OGEN OGS OIA OI OHI OII OIS OKLO OKE OKTA OKYO OKUR OLED OLLI OLMA OLB OLN OLO OMCC OM OMAB OMC OMCL OLPX OLP OMER OMF OMGA OMH OMEX ON ONBPP ONB ONBPO ONCO ONCY OMI ONEW OMIC ONDS ONFOW ONFO ONIT ONMD ONMDW ONTO ONON ONTF ONVO ONL OOMA OP OPAD OPAL OPBK OPEN OPCH OPHC OPOF OPI OPFI OPK OPP OPINL OPRA OPRT OPTT OPP^B OPT OPTX OPP^A OPP^C OPRX OPXS OPTXW OPY OR ORA ORGN ORCL ORGO ORGNW ORI ORIC ORC ORKA ORKT ORLY ORN ORLA ORRF ORIS ORMP OSK OS OSCR OSIS OPTN OSPN OSS OSBC OSTX OSUR OSW OTLY OTLK OTIS OTEX OTRK OUSTZ OST OTTR OUST OUSTW OVBC OVID OUT OVV OWLT OWL OXBR OVLY OXBRW OXLC OXLCI OXLCP OXSQ OXLCZ OXLCO OXLCN OXSQG OZK OZ OXSQZ OXY PAA OXLCL OXM PACK PAC PAAS PAG PAGS PACB PACS OZKAP PAHC PAL PAI PALI PAGP PALT PAMT PANL PANW PAM PAR PARA PATH PATK PASG PARR PARAA PAPL PAVM PAVS PAVMZ PAXS PAY PAYO PAX PAYX PBBK PBF PAYC PB PBA PBH PBFS PBI PBHC PBM PAYS PBPB PBR PBT PC PBMWW PBYI PCG PBI^B PCB PCAR PCF PCG^A PCG^B PCG^G PCG^I PCM PCG^H PCH PCN PCK PCG^D PCG^E PCG^C PCQ PCOR PCRX PCSA PCTTU PCTY PD PDCC PCTTW PDCO PCT PCG^X PDFS PCYO PCVX PDI PDEX PDLB PDPA PDD PDSB PDM PDT PDYN PDO PDYNW PEB PDX PDS PEB^F PEBO PEB^E PED PECO PEN PEB^G PEGA PEG PEBK PEB^H PEP PENG PEPG PEO PERF PERI PENN PESI PETWW PET PETS PETZ PEV PFE PFC PFBC PFG PFD PFH PFGC PFIS PFIE PFLT PFL PFO PFN PFS PFSI PFXNZ PG PGC PFX PGHL PGNY PGR PGY PGRE PGEN PGP PHAR PH PGZ PGYWW PHGE PHIN PHG PHI PHAT PHD PHK PHLT PHIO PHR PHM PHT PHX PI PII PHUN PIII PINS PHVS PIIIW PIM PINE PJT PITAW PIPR PKBK PITA PKG PKE PK PKST PKX PL PLAB PLAO PLAG PLBY PLBC PKOH PLL PLCE PLMJ PLAY PLD PLMR PLG PLNT PLOW PLMJW PLRZ PLUG PLTK PLRX PLTR PLSE PLUR PLPC PLX PLXS PM PLYA PMCB PLUS PMEC PINC PMF PMM PLYM PMAX PML PMN PMNT PMO PMTS PMT PMT^C PNBK PMTU PMT^B PMVP PNC PMX PMT^A PNF PNFP PNFPP PNI PNST POAI PNW PNTG POCI PNNT PNRG PODD POET PODC PNR POLA POLE POLEW POOL PONY POR POWI POLEU POST PPBI PPBT POWWP POWL PPG PPIH PPL PPC PPT PPTA POWW PR PRAA PRA PRAX PRCH PPYA PPSI PRCT PRENW PRFX PRE PRDO PRGO PRH PRGS PRI PRG PRIF^D PRLB PRK PRKS PRIF^H PRIF^F PRIM PRIF^I PRLD PRIF^L PRIF^K PRIF^J PRMB PROCW PRM PRO PROF PRME PROK PRPH PROC PRPL PROV PROP PRQR PRS PRPO PRT PRTA PRTH PRTC PRU PRTS PRTG PRSO PRZO PSA PRVA PSA^G PSA^I PSA^H PSA^F PSA^J PSA^M PSA^Q PSA^O PSA^K PSA^L PSA^P PSBD PSA^N PSA^S PSEC PSA^R PSF PSHG PSFE PSMT PSNL PSIX PSNYW PSIG PSN PSEC^A PSQH PSTL PSTG PSTV PSTX PSO PSX PTA PTC PSNY PTCT PTGX PT PTIXW PTEN PTHL PTLE PTLO PTMN PTIX PTON PTN PTPI PTVE PUBM PUMP PULM PUK PVBC PVH PVL PVLA PTY PW PWR PWOD PWM PWUPW PX PYN PYCR PWP PYPD PXLW PW^A PXS PXSAW PYT PYPL PZC PZZA PZG" 

prompt_str_8 = "QCOM QCRH PYXS QDEL QETA QD QETAR QBTS QGEN QH QIPT QLYS QMMM QFIN QNRX QLGN QNCX QNTM QNST QQQX QMCO QRTEA QS QSG QRTEP QRVO QSI QSR QRHC QRTEB QSIAW QTRX QTI QTWO QTTB QUAD QUIK QXO RA QURE QVCC QVCD QUBT RADX RAIL RACE RAMP RANI RARE RAVE RAPT RAND RAY RANGU RAPP RAYA R RBA RBBN RBCAA RBLX RBC RBB RBOT RBRK RBKB RCAT RCC RCB RCD RCEL RC RC^E RCKT RCG RCL RCMT RC^C RCON RCS RCKTW RCUS RDAC RCKY RDACU RCI RDCM RDHL RDDT RDN RDNT RDUS RDFN RDWR RDVT RDIB RDI RDW RDZN RDZNW RDY REAL REAX RECT REFI REBN REFR REGCO REE REGN REI REGCP RELI REKR REG RELL RELIW RENB RELY REPL REPX RENT RENE RELX RERE RENEW REVBW RES REVB REXR REX REVG RETO RF REZI REYN REXR^B REXR^C RFACW RFAIR RFACU RFAI RF^E RFAIU RFI RF^C RFL RFIL RF^F RGA RGLD RFM RFMZ RGLS RGCO RGEN RGF RGNX RGC RGR RGS RGP RGT RGTI RGTIW RH RHI RICK RHP RHE RILYK RHE^A RIG RILYG RILY RILYM RIGL RILYN RILYL RILYP RILYT RIO RIOT RIME RITM RITM^C RITR RITM^D RILYZ RIV RITM^A RITM^B RIVN RJF RJF^B RIV^A RKDA RLI RLAY RL RKT RKLB RLJ RLMD RLGT RLTY RLX RLYB RM RMBL RMCO RMAX RMBS RMCF RLJ^A RMBI RMCOW RMI RMD RMSG RMR RMSGW RMMZ RMNI RMM RNAC RMT RNA RMTI RNG RNAZ RNP RNGR RNR RNW RNR^F RNWWW RNR^G RNST ROIC ROG ROIV ROCK RNXT ROK ROAD ROOT ROMA ROLR ROL ROP RPAY ROKU RPID ROST RPM RPRX RPD RRGB RQI RRC RPTX RRBI RRX RPT RS RSG RR RSF RSI RSKD RRR RSLS RTC RTO RSVR RSSS RUMBW RUM RSVRW RUSHA RVLV RTX RVMD RUN RVNC RVP RVPH RVPHW RVSB RVMDW RUSHB RVSNW RVSN RVT RWAYZ RWAY RVYL RWAYL RWT RVTY RWTN RXO RWTO RWT^A RXST RXT RY RXRX RYAAY RYAM RYDE RYI RYN RYTM RYAN RZC RZB RZLT RZLVW SABA S SABR RZLV SABSW SACC SA SAFE SAFT SABS SACH SAIHW SAIH SAIA SACH^A SAIC SAG SAGE SAH SAJ SAM SAMG SAN SANG SANM SAND SANW SANA SARO SAP SASR SATLW SATL SAT SAY SAR SAVA SATS SATX SB SAZ SBBA SBC SBCWW SBET SBAC SB^C SB^D SBFG SBCF SBEV SBFMW SBFM SBH SBLK SBGI SBI SBR SBS SBSI SBXD SBUX SBT SBRA SCCC SCCD SCCG SCCE SCCO SCD SBSW SCCF SCHL SCE^J SCE^N SCE^M SCE^G SCKT SCI SCHW SCE^K SCE^L SCHW^D SCLX SCL SCHW^J SCM SCNI SCNX SCPH SCLXW SCOR SCVL SCWX SCWO SCSC SCPX SD SCS SDAWW SCYX SDA SDGR SDHY SDRL SDOT SDIG SDHC SDST SDSTW SE SEE SEATW SEED SEB SEDG SEAT SEAL^A SEG SEI SEIC SEAL^B SENEA SEER SENEB SEMR SEM SENS SEPN SER SELF SERA SES SEZL SEVN SERV SFBS SFB SFBC SELX SF SF^B SF^C SFL SFM SF^D SFIX SFHG SG SFST SFWL SGA SGC SGBX SGD SGLY SFNC SGHC SGMT SGHT SGMO SGMA SGRP SGML SGU SGN SGRY SHAK SHBI SHC SHCO SHEN SHEL SHFS SHG SHFSW SHLT SHIP SHMD SHLS SHIM SHMDW SHO SHOO SHOP SHOT SIBN SHYF SHO^I SHW SIDU SHO^H SIF SHOTW SIEB SID SHPH SIFY SIGI SIGA SIGIP SIG SILA SILV SIMAU SILC SII SIMA SIMAW SILO SIMO SIM SINT SITC SIRI SITE SJ SISI SJM SITM SKE SJW SKGR SJT SKIL SKGRW SKK SKIN SKM SKLZ SKWD SKYE SKX SKT SKYT SKYH SKYQ SKYX SKYW SLAB SLB SLDB SLDPW SLE SLDP SLG SKY SLM SLGL SLI SLGN SLF SLN SLNHP SLNH SLNG SLND SLRN SLMBP SLQT SLRC SLNO SLP SLSR SLS SLG^I SLVM SLXN SLRX SMAR SM SMBC SMC SMBK SLXNW SMCI SMFG SMHI SMG SMP SMRT SMID SMR SMPL SMSI SMTI SMTK SMX SMXT SMWB SMTC SMXWW SN SNAP SNAL SNAXW SNBR SNAX SNCRL SNCR SNCY SND SNDA SNDX SNDL SNES SNEX SNA SNGX SNN SNDR SNOA SNFCA SNPX SNRE SNOW SNPS SNTI SNSE SNV SNT SNTG SNYR SNY SO SNX SOAR SOFI SOC SOBO SOGP SNV^E SOBR SOHOB SOHON SNV^D SOHO SOHOO SOJC SOHU SOJE SOJD SOLV SON SOND SONDW SONN SONM SOL SONO SOPA SOR SOS SOPH SOTK SOUNW SPAI SONY SOUN SPB SOWG SPCB SPE SPCE SPGC SPFI SPGI SPHL SPHAU SPE^C SPH SPIR SPI SPHR SPG SPMA SPMC SPKL SPG^J SPOK SPOT SPNT SPLP^A SPLP SPPL SPNS SPNT^B SPR SPRU SPRY SPRB SPRC SPRO SPXC SPSC SPT SPXX SPWH SPTN SQFT SQFTP SQFTW SQ SRBK SRE SRCE SR SRFM SREA SQM SRAD SR^A SQNS SRDX SRM SRL SRTS SRPT SRG SRRK SRI SRZN SRG^A SSB SSBI SRV SSP SSL SSBK SRZNW SSNC SSKN SSRM SSSSL SSD SSSS SST SSTK STAA STAF SSY ST STC SSTI SSYS STBX STBA STCN STAG STE STEL STEP STEC STEW STEM STG STHO STGW STIM STFS STK STI STKH STKL STM STLD STOK STKS STN STLA STRA STNE STNG STRL STRO STR STRR STRT STRW STRS STRM STSS STRRP STSSW STVN STWD STTK STT SU STXS STT^G SUGP SUM SUI STX STZ SUNE SUNS SUPN SUZ SUP SUN SVC SUUN SURG SVII SVCO SUPV SVIIW SVM SVRE SVMH SVMHW SVREW SVT SW SVRA SWBI SVV SWI SWAG SWAGW SWIN SWKH SWIM SWTX SWKS SWVLW SWVL SWX SWK SWZ SWKHL SXT SXTC SXC SXTPW SXI SXTP SY SYBX SYK SYBT SYF SYF^A SYNA SYF^B SYNX SYRA SYRE SYRS SYPR SYT SYM SYTA SYY SYTAW" 

prompt_str_9 = "T TAC TAIT TAK TACT TALO TALK T^C TANH TALKW TAL TAOP T^A TASK TARS TAVI TARA TAP TAYD TBB TBBB TATT TBBK TBLAW TBLA TAVIU TBI TBMC TBLD TBMCR TBN TBPH TBRG TCBIO TC TCBP TBNK TCBI TCBX TCBS TCBPW TCMD TCPC TCBK TCI TCRT TCRX TCTM TCOM TDF TCX TDG TD TDOC TDACU TDS TDC TDTH TDUP TECK TECH TEAF TDS^V TDS^U TECTP TEF TEAM TDW TECX TDY TEI TEL TELA TEM TEN TEO TENB TERN TELO TETE TENX TER TETEU TETEW TEN^F TEVA TEX TEN^E TFII TFC TFSL TFSA TFINP TFIN TFC^R TG TFC^I TFX TFC^O TFPM TGI TGLS TGL TGS TGB THC TGT THCH TGNA TGTX THM THAR THFF THG TH THO THQ THRD THRM THRY THS THTX THR TIGO THW TIGR TILE TIMB TIL TISI TIPT TIVC TIRX TIXT TKLF TKC TJX TITN TKNO TLF TKO TLK TKR TLN TLS TLSA TLPH TLRY TLSI TLSIW TLYS TM TMCI TLX TMC TMDX TMCWW TMO TMP TMHC TMQ TMUS TME TNET TNGX TNFA TNL TNDM TNK TNC TNMG TNONW TNON TNXP TNYA TOIIW TOMZ TOP TOL TOON TORO TOUR TOI TOWN TOPS TOST TPB TOYO TPCS TPET TOVX TPC TPG TPIC TPR TPL TPH TPGXL TPST TPX TR TPTA TRAK TRDA TRC TREE TRAW TRIN TRIB TREX TRGP TRINI TPVG TRI TRINL TRINZ TRIP TRMB TRMD TRNO TRNR TROW TROO TRMK TRN TRNS TROX TRML TRP TRSG TRS TRT TRST TRTN^C TK TRUP TRU TRTN^D TRTN^E TRTN^A TRTN^B TRUE TRUG TRV TRVG TRTX^C TRX TSBK TSAT TSE TRVI TSCO TSBX TS TSI TSHA TSEM TSLA TSM TSN TSLX TSVT TSQ TT TTAN TSSI TTE TTEC TTD TTEK TTI TTMI TTC TTGT TTNP TTOO TTSH TTWO TU TURB TUYA TURN TVE TVC TUSK TVGN TVTX TVGNW TV TW TWFG TWG TWI TWLO TWN TWST TX TWIN TWO TWO^C TXNM TXN TXMD TWO^A TWO^B TXO TXT TXRH TXG TRTX TY TYL TYRA TYG TZOO TZUP TYGO UAL TY^ UA UAA UAMY U UBCP UBS UAVS UAN UBER UBSI UBFO UCAR UBXG UBX UCB UCL UCTT UDMY UDR UE UEIC UFPT UEC UFPI UFCS UGI UCB^I UG UFI UGP UHAL UHGWW UHS UGRO UHG UIS UI UHT UL ULBI UK ULTA ULY ULCC UKOMW ULH UMAC ULS UMBF UMH UMC UNB UNF UNCY UNFI UNH UNIT UNMA UNM UMH^D UNTY UOKA UNP UONE UPC UPBD UONEK UP UPLD UPB UPS UPST UPWK UROY URI URGN UPXI URG USAP URBN USAC USAS USB USAU USA USEA USCB USB^P USGOW USB^Q USFD USB^H USB^A USB^R USEG USB^S USLM USIO USNA USGO UTG UTF UTL UTI UTHR USPH UTMD USM UTZ UTSI UUU UVSP UVV UWMC UVE UXIN UZE UUUU UZF UZD V VABK VACH VANI VACHW VALU VALE VALN VATE VAL VAC VBF VBFC VBNK VBTX VCTR VCICU VCEL VCV VCIG VCYT VCIC VC VCICW VECO VCSA VEEA VENU VEEE VEL VEEV VEON VERB VEEAW VERO VERV VERU VERA VERI VERX VFF VET VFS VFC VGAS VFSWW VGI VGASW VFL VGZ VIAV VIASP VIGL VICI VGM VHC VICR VHI VINC VINE VINP VIK VIRC VIRT VITL VIST VIOT VIPS VIV VIR VIVK VISL VKI VIRX VKQ VLGEA VLCN VLO VKTX VLN VLT VLTO VLYPN VLYPO VLRS VLYPP VMC VLY VMAR VMD VMEO VNCE VMCA VMO VMI VNDA VNET VMCAW VNO VNT VNOM VNRX VOC VNO^N VNO^O VOR VOXR VOXX VNO^M VNO^L VPG VOYA VOD VRAR VRDN VRCA VRA VPV VREX VRE VRAX VRME VOYA^B VRMEW VRN VRNA VRSN VRRM VRPX VRTS VRNS VRT VRNT VSAT VSEC VSCO VRTX VS VSME VSH VRSK VSEE VSEEW VST VSTE VSTEW VSTA VSTS VTEX VTLE VSTM VSSYW VTAK VTGN VTN VTR VTRS VTMX VTOL VTYX VVI VTSI VTVT VVOS VUZI VVPR VTS VVX VXRT VVV VVR VZ VYGR VYNE VYX WAB W WABC VZLA"

prompt_str_10= "WAI WAFD WAFDP WAFU WAL WAVE WALDW WATT WALD WAT WASH WAY WAL^A WAVSW WAVS WB WBD WBA WBTN WBS WBUY WBX WBS^G WD WCC WCN WDAY WCT WDH WBS^F WCC^A WDFC WDC WEA WEC WDI WEN WEAV WERN WDS WELL WES WEX WEYS WETH WEST WF WFC WFC^A WFC^Z WFRD WFC^D WFCF WFC^C WGO WGS WGSWW WFC^L WFG WFC^Y WHF WHFCL WH WHG WHLRP WHLM WHD WHLR WHR WILC WHLRD WIA WINVU WISA WIT WINA WINV WIMI WING WINT WIX WK WKC WIW WKEY WKHS WKSP WLDSW WLACU WLDS WLDN WLK WLY WLFC WLYB WMB WLGS WMG WLKP WM WMK WMS WMT WNEB WNC WMPN WNS WNW WOLF WOR WOOF WORX WPC WPRT WOK WRAP WOW WPP WRB WPM WRB^E WRB^F WRB^H WRD WRLD WRBY WSBC WS WSBCP WRB^G WRN WSM WSC WSBF WSFS WT WSO WSR WTBA WST WTMA WTFCM WTFCP WTFC WTI WTM WTRG WTO WTTR WTS WU WVVIP WULF WTW WVVI WW WWD WWW WYHG WWR WY WVE WYY X WYNN XBIO XBIT XAIR XEL XELB XCH XCUR XBPEW XERS XENE XBP XFOR XIN XGN XFLT XHG XHR XLO XOM XNET XFLT^A XMTR XOSWW XOMAP XOMAO XPEL XOS XP XPEV XPO XPL XPER XOMA XPOF XRAY XPRO XRTX XNCR XPON XRX XTKG XWEL XXII XYF XTIA XTNT YAAS YCBD XYLO XTLB YALA XYL YETI YEXT YGMZ YI YJ YELP YMM YHGJ YMAB YCBD^A YORW YOTA YOSH YIBO YOU YRD YQ YHC YPF YOTAW YSXT YSG YTRA YXT ZAPP YYAI YUM ZBAI Z YY YUMC ZAPPW YYGH ZBAO ZCAR ZBRA ZD ZCMD ZDGE ZENA ZBH ZBIO ZENV ZCARW ZEO ZEOWW ZETA ZEPP ZGN ZH ZIM ZEUS ZION ZIMV ZG ZIONP ZI ZJK ZIP ZK ZJYL ZKIN ZKH ZLAB ZM ZNTL ZONE ZOOZ ZSPC ZOM ZS ZTO ZOOZW ZTEK ZTR ZUO ZUMZ ZVIA ZURA ZTS ZVRA ZVSA ZYME ZWS ZYXI"


prompts = [prompt_str_1, prompt_str_2, prompt_str_3, prompt_str_4, prompt_str_5, prompt_str_6, prompt_str_7, prompt_str_8, prompt_str_9, prompt_str_10]
data_arr = []

# download closing price data 
with concurrent.futures.ThreadPoolExecutor() as executor:
  futures = {executor.submit(downloadData, prompt): prompt for prompt in prompts}
  for future in concurrent.futures.as_completed(futures):
    try:
      data = future.result()
      # cols = data.loc[:, pd.IndexSlice['Close']]
      data_arr.append(data)
    except Exception as e:
      print(f"Error occurred for prompt {futures[future]}: {e}")

# store outputs in separate CSV files
k = 0
for df in data_arr:
  cols = df.loc[:, pd.IndexSlice['Close']]
  fname = "sample_data_"+str(k)+".csv"
  cols.to_csv(fname, sep='\t')

  k += 1
