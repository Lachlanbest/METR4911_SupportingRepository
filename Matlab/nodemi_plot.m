AUTSL_jm = [0.38654763 0.38512276 0.36547708 0.35336265 0.32711225 0.33274485...
    0.27498803 0.33214724 0.32394863 0.32639752 0.32500987 0.3264435...
    0.32398211 0.32698294 0.3221432  0.32677346 0.32202219 0.27466612...
    0.26513457 0.2659775  0.26134952 0.26579923 0.26166374 0.2648509...
    0.26111988 0.2640978  0.26140978];
IsoGD_jm = [0.36280723 0.36406822 0.33294271 0.32370607 0.28219232 0.30612083...
    0.26608099 0.30633338 0.29557983 0.29550526 0.28626235 0.29622266...
    0.3004591  0.29449257 0.2994219  0.29403275 0.28871559 0.26669733...
    0.26042619 0.26354588 0.26052237 0.26337449 0.2651787  0.26211003...
    0.26459922 0.26114695 0.2586582];
ConGD_jm = [0.35756957 0.35774907 0.32216343 0.31061511 0.25607537 0.30285543...
    0.2459692  0.30453128 0.2924249  0.28306624 0.27369794 0.28470287...
    0.29470455 0.27861504 0.29224492 0.2830362  0.27549065 0.24746566...
    0.24352147 0.24293985 0.24113224 0.24248334 0.24806665 0.24500022...
    0.24676965 0.24311534 0.24015477];
LSE_jm = [0.36182112 0.35149316 0.35945912 0.29571254 0.33231699 0.25021201...
    0.28707573 0.25013825 0.22984409 0.23371616 0.22555599 0.23504894...
    0.226651 0.23459686 0.22873497 0.23420141 0.22962135 0.28680549...
    0.26850972 0.2729137 0.2633341 0.27289486 0.26608953 0.2710564...
    0.26761829 0.2722975 0.26608766];
IsoGD_bm = [0.36280723 0.33958774 0.31945628 0.31206839 0.27345073 0.28762571...
    0.25269071 0.36735582 0.27941091 0.28221323 0.27871458 0.28297926...
    0.28851347 0.28087215 0.28582973 0.27884611 0.28359882 0.36689303...
    0.24513235 0.25229784 0.25364296 0.25260258 0.257075   0.25226624...
    0.25721892 0.25107719 0.25938104];
AUTSL_bm = [0.38654763 0.37754162 0.35854528 0.34758269 0.31508719 0.32381633...
    0.27093346 0.37651744 0.32955072 0.33530672 0.33570907 0.335749...
    0.33252782 0.33598649 0.33279527 0.3351707  0.33832614 0.36821571...
    0.27368233 0.28402824 0.27977906 0.28487021 0.27778889 0.285339...
    0.28205445 0.28323479 0.29426834];
ConGD_bm = [0.35756957 0.33410152 0.30725755 0.29773666 0.24401687 0.27122106...
    0.22219857 0.35939095 0.26570269 0.26366033 0.26130871 0.26495337...
    0.27675214 0.25994518 0.26825192 0.26131734 0.26519032 0.36288588...
    0.22350569 0.2267111  0.23290922 0.22708948 0.23656897 0.22868202...
    0.23932523 0.22650808 0.24142175];
LSE_bm = [0.36182112 0.32655033 0.3405758 0.28018489 0.3186168 0.24225481...
    0.27705692 0.3781921  0.22919637 0.24408529 0.2347333 0.24511715...
    0.23570822 0.24515447 0.24165562 0.24503105 0.25507588 0.36945617...
    0.26756261 0.28140707 0.27346882 0.28061084 0.27243702 0.27948542...
    0.27417726 0.28237541 0.28736824];

nodes = 1:27;

subplot(121);
plot(nodes, AUTSL_jm);
hold on;
plot(nodes, IsoGD_jm);
title({'Joint Motion Data Average Localised Mutual Information','per Node for AUTSL & IsoGD Dataset Test Splits'});
xlabel('Node Number');
ylabel('Average Localised Mutual Information');
legend('AUTSL', 'IsoGD');
subplot(122);
plot(nodes, LSE_jm);
hold on;
plot(nodes, ConGD_jm);
title({'Joint Motion Data Average Localised Mutual Information','per Node for LSE eSaude Uvigo & ConGD Dataset Test Splits'});
xlabel('Node Number');
ylabel('Average Localised Mutual Information');
legend('LSE eSaude Uvigo', 'ConGD');