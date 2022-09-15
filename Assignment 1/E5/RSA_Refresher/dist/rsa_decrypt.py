from math import lcm

p = 123809087791774272410895685738016241740435722604791146995280097623158924445443186868671503289475401755964076309115709831500902283567453926772932321500881735346956473490736691081076208249404478120909604255779527144397384589776343740334674453963366677129782104359036266657020225305275876169069038984135961048621
q = 121556184828980721181814168042887601238542270820451991702290982443494506717531711393684140304007704946391345689945066374411034213067405713402016477204710255399745250668871431789853297448271929657706766742507382533002856586545528789882478741210737027533906783713571540995602771797162394747952776365010741182527
e = 65537
c = 1197647896549075012453297616670026035100253013255918589557271910601511411331923987631815768017321883173381774857255918076382968167925258588152179360405539429552006183217607724737760713061641551718563306776291952834549775895369095091523955114253782839478575297245778886911641862954334458719393421428080508714988122960188017662999935534635220901093812673907783260634834009159160861189689841167055361688938329686473921446287635844940155265471308349018589139861908905167674954841818459729156071882605676679278691922521150970929184109144419426701906754903440245112134837176603718998238487467589859708263646094259181791476

n = p * q
phi = lcm(p - 1, q - 1)
d = pow(e, -1, phi)

m = pow(c, d, n)

print(m)
