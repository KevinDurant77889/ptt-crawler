from bs4 import BeautifulSoup
import urllib.request as r
import re
import os
from tkinter import *
from tkinter.filedialog import askdirectory
import tkinter.scrolledtext as tkst
import threading
from tkinter import messagebox
import os
import base64
icon = '''AAABAAEAMDAAAAEAIACoJQAAFgAAACgAAAAwAAAAYAAAAAEAIAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAaK0n/HTtc/x5BaP8dQWb/bZet/7Tr/P94udj/Uo+9/5rF3v/R6Pv/2uv8/9rr/P/X6/z/
2ev8/83d6/8qNUT/KTpT/ypEY/8qQmf/Hjxf/5Gszv+csu//mLDv/5uw6/+NpN7/mLPv/5Ot9f+S
sPL/kJ3C/7K1sv+3tLL/oqOk/3x/hv8sM0D/n6ex/9jr+//b6vz/2+v8/9vr/P/Z6vv/1Of7/4Sp
xf9MbJH/RE5k/4+do/+dqav/namr/52pq/8KFjL/EStG/xc3WP8iQmX/bZSp/7bs/P96utj/VZnS
/1WSwf+Ap8r/w9zt/83l+P/E3e//mK7C/1dth/8pQV7/JkBn/ydCbP8jPmb/JEVu/4ik2v+asfH/
j6fY/5mtzf+0yef/gZvE/5Ou6v+WsPT/g5S//7G2uP+6uK7/ubav/3uAhf8XKTv/pbXH/9Hn+f/Z
6fn/2ev6/9ft+v/B2ur/fKHB/1qTwv9AZpX/RE5m/5Gco/+dqar/nair/5yoqv8QIEX/AxMw/xQm
Q/8cMlL/ao+i/7br/P96utf/UZfR/06Y0P9blsn/IkZl/zFMa/8pRWb/KEVn/yZDaf8gQ2b/Hj5n
/x4/a/8cPWn/M1WD/5Os4/+Qpc7/us3m/9fm+f/Y6Pn/zN72/4idyf+LpN7/b4e5/5ept/+6trH/
u7et/3+GiP8VKkX/LUdm/z1aeP9le5L/pcHN/53J0/9wor7/XJrK/1OZ0v87ZJf/RE5l/5Gbo/+b
p6j/nKer/5yoqv84VoT/GS5T/wMPMP8TIUD/ZoWX/7bs/P95uNj/UpjT/0uY0/9SldD/GEFs/yFB
av8dPGj/Hz9r/x5Aaf8cQGf/Gz5m/x5Aaf8bPGj/UnGZ/5aqzf/P4PL/2ur4/9vo/f/b6f3/3On7
/9Ti+v+ardH/Y3uq/3SOrv+ytLn/urms/4CIif8SKEj/JURq/yJFbP8oSGj/vOPz/7Xt+/94utr/
TJfQ/0uX0v86ZZb/RE5l/5KcpP+bp6j/nKer/5unqf8yV4f/OFmI/yU+aP8EEjT/XHeK/7Xs/P94
uNj/UpfS/02X0v9Uls//GUBu/xw/af8bPGf/Hz5q/yBAaf8eQWn/G0Bo/yJDaf8tSGr/lKzF/9fo
+//b6fv/2ur8/9vp/v/a6v3/2+v8/9zq+//W4/n/qLrf/2F7ov+apLX/tret/4KIh/8TJ0n/JkNs
/yBCbP8eRmf/rtrt/7bq/P+Bwd3/TZjP/0qXz/87Zpb/Q05l/5Kdo/+cqKj/nKir/5uoqv8/XoD/
OFqH/zVaif8uTnX/W3mO/7Xr/P95uNn/UZfR/0yX0/9TmNL/G0Bv/xw/av8ePGj/ID5p/yI/av8f
QGz/IkFr/ytHaP+VrL//1+r5/9rp/f/b6f//2+n//9vp///b6v3/3Oz9/9vr/f/a6f3/1uX8/7PJ
5/96iqj/q7G6/32Fif8UJ0n/JkJr/x9Aav8hSGv/ncna/7Xq+/+Fx+D/TZnQ/0qY0f89Zpn/RE1l
/5Gcn/+dqar/namq/5unqf96jZz/RGB+/zlahv8yXof/a5Gp/7bq+/95ttj/UZfR/0yX0/9Sl9H/
Gz9v/xw/av8ePWj/IT5q/yI/av8lQm3/M0pu/6i90//Y6/r/2uz7/9rp/f/a6P7/2uj+/9ro/v/a
6fz/3Oz9/9vr/f/a6vz/2+v7/9bn+v+5yen/hZOw/258lP8UKEv/I0Jq/x9Ba/8gR2n/j7rM/7Tq
+v+KyuL/TpfP/0uX0v9BbqL/RExk/5Ccnv+dqar/nKiq/5qnqf+eqK3/hpel/09jg/9BYIb/apKr
/7Xr+v92ttj/WJ7W/0uV0f9Sl9H/Gj9u/x0/av8fPWj/IT9p/yA+aP8pRWj/n7XI/9jm+P/a6P3/
2ur8/9rp/f/a6P7/2uj+/9vo/v/a6Pv/2+v8/9vq/P/a6fz/2+v8/9rp/P/W5fz/tsnm/2JznP8U
KE//IUFr/x1Aav8eRGj/gKq+/7bs+/+QzeX/UJbP/0uX0/9FeK3/RU9m/5Gbnv+dqar/m6ep/5qn
qf+hp6v/nKet/5KhrP9dcIb/cpWo/7Ps+/9ytNb/bLHb/0yWz/9UmdD/ETJf/xw6Xv8fP2P/IkFk
/yFBaf9wiaT/0OP4/9fn+v/X6Pz/2Oj8/9rp/v/b6fz/3Or8/9jk9//Q3O7/3er6/9ro+v/a6f7/
2+n+/9vp/f/Y5v3/0ub9/6q/5/82TH7/IkFs/yFAbf8gQm3/cJeu/7ft+f+V0un/VJjR/0uW1P9J
frP/RE5m/5Sbof+bp6f/m6ep/5qmqP+hqKv/oqmr/6Orq/+cqLH/i6q1/7Ps+v9ytNX/e8Di/06Y
z/9XmM7/Cx9I/xYpR/8bNVb/JkBp/ydBav+4zej/z974/9Hd+f/T4vz/1uX8/9no/P/c6/3/1+X3
/9bj8v/Y5fT/ztvr/9vo+//a6f7/2uj+/9nn/f/V4/z/1OP7/8PW9/92j8D/JEJy/yE/b/8fP2//
X4Sg/7br+v+Z1+z/VJjO/0yX0/9Nhrr/Qk5o/5SbpP+cp6n/m6ep/5mmqP+gpqr/oair/6OpqP+j
qqz/m7i9/7fr/P93uNP/is/q/0+Zz/9Rls7/DSZQ/wURMv8PJ0n/KD1s/01fif/L2Pr/y9P7/8zU
+//O2/z/1OL8/9nn+//b6/z/2Of2/8DN2/+9ytr/0d3t/9zq/P/a6f7/2ef9/9fl/P/R3vv/zdv6
/8zZ+v+ds+b/M02E/y5KgP8gP3T/SWyO/7Xq+v+e3PD/VJrM/0yW0f9VkcT/P01p/4+YpP+bp6r/
m6ep/5mlp/+gqaz/oKmr/6Kpqf+iqqr/nbW9/7Pr+/99v9T/lNju/1CazP9Qls7/KleJ/x0yWv9g
cJj/qr3r/6Cw2f/G0Pv/xMr9/8bO/P/K1fz/0uD7/9jm/P/a6vv/3Or6/9zq+v/a6Pj/3Oj6/9vp
+v/a6f3/2Oj9/9Pi/P/N2fv/xdP5/8fS+/+vv/P/hp7Y/5aw7v9Ycqv/OFV9/7rq+f+m5PX/VpvK
/0yY0P9npNL/QFBu/4+aov+apqj/maao/5ekpv+fqKz/oKqr/6Kqqf+jq6r/nbW9/7Ps/P+Hydz/
nN7w/1Kby/9Slc3/LluH/3KLqf/M3PX/utHz/6i22/+8xvT/v8X6/8LJ+v/H0fz/0d37/9fm+//a
6vv/3er7/9ro+f/U4vL/3Oj7/9vq+v/a6fz/1+f9/9Hf/f/K1fv/wMr1/8HK+P+3xfb/d4zI/4ih
4v+Ur+n/PlqG/7fk9P+s5/n/W53M/1Gb0f9xrtf/SFt6/4+bov+apqf/mKWo/5ilp/+ep6v/oKmq
/6Kqqv+jrKr/nLS7/7Ps/P+Oz9//pePz/1Scyv9Rk8n/UHWT/8HY6/+KoMT/eo6//7zH6v/Dy/r/
xcz7/8fQ+//K1Pz/0d76/9fm/P/b6/z/3Oj5/9vp+v/D0eD/3Oj6/9zq+v/b6f3/1+f9/9Hg+v/N
1/r/zNP7/8fO+v/C0fr/i57Z/5Wt7v99mtX/fJjK/6PM4/+y6/v/YqPO/1Kdzv93uNr/TGaH/4ya
o/+Zpqj/l6Sm/5ajpf+gqaz/n6iq/6Oqq/+jqqv/nri+/7Ps+/+Y1uT/qeb2/1ecy/9Pj8T/o8HW
/6m+1v+Jpd3/h5zL/9Lg+f/N2/r/y9X4/87Y9//T2/n/1OH4/9fm+//c6vz/3On6/9vo+v/b6Pn/
3en7/9zq+//b6Pz/1+f8/9Xk9f/Y3/f/09r2/9HY+P/K2vz/mKng/3aMyv+Oq+j/f5vS/4qv0f+z
6vn/bq/U/1OfzP97v93/RWeI/4uZpP+YpKj/lqOm/5ajpf+gqaz/nqeq/6Oprf+iqa3/ob3D/7Pt
+/+e2uf/quf4/1ebzP9RjsD/yuX3/5221P+Fodr/mrLY/9Tl+//Y4/b/oJqj/8Kwqv+dm5z/z9no
/9vq/P/d6f3/3un7/93p+//c6Pr/3Oj7/9zq+//b6Pz/2+j6/6KkrP+nmI3/sJ+R/6iiqP/X4vr/
ma3b/4ac1f+AmtP/hZ3R/4On0f+z6vr/drbY/1aizv+DxuL/RG2Q/4uZpv+YpKr/l6Op/5aipf+g
qaz/n6ir/6KorP+gp63/mre//7Ls+/+h3Ov/quf5/1acy/9YkL7/vtfx/5Ku1v93lMz/mrDQ/9rn
+f/Bxc7/gmRS//C/kv/g0K7/2dbZ/+Dq+v/d6f3/3un7/97q/P/d6fv/3en7/9zq+//c6fz/5e36
/3RoZf/htYz/6cKQ/9zTvP/m6vX/r8Dn/150q/+Kotb/q8Lu/4en2P+16vr/fb3c/1ej0P+Lz+f/
QnSc/4aXqf+Xo6j/lqKo/5Wipf+gqaz/n6ir/6GorP+hqa//jKq0/7Hs+/+k3+//qub4/1ecyv9V
ibX/sMjq/5Wx7f+WsvH/qr7b/9vn9f+SlJr/sYBx/4ZMKv++i2n/noeA/+Ls+f/d6fz/3un7/93o
+v/d6fv/3en8/9zq+//d6f3/6O/4/2RWUf+3fmP/jVMy/51zW//Kyc3/v9Dv/2aAuP+UsOf/m7fr
/4ik2P+56vr/hMTg/1um1P+R1uz/SICt/3uRpv+Voab/laGn/5WhpP+cqKr/namr/5+qrf+gqrD/
iKez/7Xr+v+k4vD/puT3/1ObxP9Kf6z/rMHk/5Wx7f+Fm9X/vM/n/73Ez/+Bgn//g0Y8/4E4Iv+M
RDH/kXFp/+Xt9//b6fv/3er9/9/p+//a6vz/2ur7/97r/P/b6/3/5Ojx/1NAPf+EQDL/hzkm/4dG
Nv+4r6//r7zX/4Kg1/9si8T/lrLt/22Luv+86/r/i8rl/1+l0/+i4fX/Uoq0/3GMpv+Voqf/lKGn
/5ShpP+cqKr/namr/5+qrf+Rnab/jrPB/7Ho9/+l4vD/peP2/1Gdx/9RhrT/jKW+/4ifxv9VaZb/
q7zQ/4eGk//MyMT/lWZd/5k8K/+VPiz/g15Z/9DW4f/Z5/r/2ej6/9zp+v/N3/D/0uL2/9jp+v/V
6/z/yMnY/+Dc2/+XYVT/njwv/4c6L/+yoKT/goSg/5a27P9RcaH/hJ3K/0hnlP+v3+//lNHo/2Op
0v+q6Pr/XJjB/1x9nP+Voaj/laGn/5WhpP+cqKr/nKiq/56prf+Fk53/jbjI/67m9f+l4vD/o+H0
/1ScyP9Ngq7/mcDM/7XR5P9ge6L/jqS6/1hZaf+qpKL/jmVe/487Mf+GPDL/Ri40/5+rvv+gscr/
zuHz/9Lk8f+VrcP/tMrr/9Ln/P/O5Pn/W2SD/2Nhbv93RED/jjwv/3w5L/+XiI//MzpT/5ez6/9a
eaj/mLze/014pP+NvdX/oNrv/2ar0P+u6vr/Y6XN/1B3nP+ToKn/laGn/5WhpP+dqav/n6ir/6Kp
q/9+kZ//k8TT/6jk8/+k4vH/ouDz/1iby/9qosf/seTv/3OasP9khbD/oL3a/y48Vv9RTVX/Wjc9
/2Y0Nv9DJzH/Q0Zi/6S42P+Jn8r/vdHp/63B0f98nrz/mLbg/8Xb9/+1yuX/kKLT/zM6Wv9DKzv/
XTY1/1AsK/88PUj/RVd3/5Wz7f9ffrP/Tnmo/12Uxv92psL/p9/x/2ms0P+t6vv/cbDS/0hzn/+Q
oar/laGl/5Whov+dqav/nqiq/6Gnqv98kqP/k8bW/6Lf7f+m5PP/ouDz/1ucy/+Autj/tOr4/2OV
tP9qk8X/b5LB/3qXxP8vSW3/MD1i/0lTcf9Uf6P/Wnmr/3SOuP+HpNj/lK3L/5ixyf9mkrz/c5TI
/6bC6P+2zuz/YHOu/2iHu/9McJr/N1By/zZDZv9BXYT/ZoGy/4er5/9Vdav/VIK1/1iYzP9vpcb/
rOT2/2uu0P+t6fv/f7zZ/0V2o/+GnKv/lKCk/5Ogov+eqav/nKiq/52nqv97l6f/jsXW/57b6v+o
5/b/oN3x/1mZxP+Uz+T/q+Hx/1CErf9vnM//VXu0/2uUy/9lncv/XpLI/2mQxP9Zmcz/bpbQ/2eL
u/+Hp+H/epnB/36jw/9Zk8b/aZHJ/3qfz/+wzfD/cYW//3mX0/9altD/YJPM/3KRzv9WhsH/aJPM
/2+V0/9rj8X/Snmr/1WZ0P9ioMj/reb3/2+xz/+u6vv/jcfh/0yEs/9ujKP/kqGm/5Chpf+dqav/
nKiq/5yoq/+An7H/jcXX/5zY6f+r5/j/ntrw/1OTu/+q5fX/mc3f/1eKuf9QfKr/Yo27/2eUxP96
utv/ZpnM/2WPvv9mosz/VoC1/zJWhP+GpOD/XICx/2OSvP9enc3/VoS7/2mXzf+HpNL/SmWY/3GT
xv9fms7/WI/D/2yXzP9ZlM3/UoG5/2mRzP9wlMr/SXiq/06Qx/9RlML/run5/3S10/+t6fr/l9Pp
/02Juf9kiKf/k6Go/4+gpf+cqKr/nair/5+prv+Ep7n/m9Tn/5jT5v+r5/j/ntnw/1mZwP+y6/v/
lcra/1WKuP9fj7f/aJm+/3GjyP+Ewt3/ZY/B/2uXvP9BeZ//TXer/013qP+Kqen/WoS9/1aIuv93
tNf/TH+1/2KYzP+Us+3/Tm2k/0Jglv80ZZj/RHio/3GXyv9dltD/TXqw/2CMwv9QdKf/U4O3/0iI
vf9LksX/od7w/3W21f+t6/v/od/x/1SNv/9fiK7/kp2o/5Cgpv+dqav/naiq/5Ogpf+XwdH/n9ru
/5XR4/+r5/n/ndju/2ajxv+z6/n/kcjV/12Qvv9bjq7/UoSl/3Onwv9spLv/LlGA/3usxf9losb/
V4jA/1qKwP+Fqev/WYrE/2CZyf+LyOL/Q3ut/2Ocyf+Ose3/W4G8/2ePxv9bkcL/T4Oq/z5ckv9C
dKv/M1uP/016rv9kjsT/UYW6/0eKwP9Pl83/j8zh/3O00v+s6vv/r+r4/1ybyf9ThbD/jp6q/5Cf
pf+dqav/naiq/42dof+n1ub/ndzv/4/N3/+p5vj/ntfu/3Kuzf+17Pj/kMnV/16Rvf94r8r/U4Sj
/5jO5P+FwNX/U4Gs/7Hp+P9srND/TYW8/1yVxf92oNv/YJnK/3Cx2P+a2Oj/U4/B/3Oy1f+Bqtz/
XIzF/1GBuv9fncr/frrZ/1yIvf9cms3/SHyr/1KEt/9Zh73/U4rA/0OIvf9QmdH/hMLZ/3S20v+r
6vv/s+z4/2Kkzf9LhLP/iZ2s/46epP+dqav/m6mp/5Gnqv+n3un/n9/u/43H3v+l4/b/ndbr/3q3
zv+27Pn/k8vY/1mQu/+EvNb/aJ+7/6/o+/+LyeH/X5W6/7Lp/P91s9j/UYy9/2agyv9rl9D/dK7V
/3vA4P+l4vL/WprL/3++4v99p9X/WorE/0N4sP9jpND/isXh/1KFuv9nq9j/U4i9/1GFuf9IerH/
U4rC/0eIw/9QmND/ebrW/22vz/+r6/v/sur6/3K01P9QjsD/d5Op/42doP+dqav/m6iq/5ixtv+m
4Ov/o+Hw/4vF3f+e3vL/m9bs/3680v+06/j/mNDe/1GLtP+FwNj/fbbM/7Lp+/+RzeP/bKXH/7Lq
+/9+udj/ZKHO/3Gs0v9ij8T/jMTj/4vM5v+u6vn/YaDN/4LD5P97qs//WIvA/0d3r/9tr9X/ks3l
/1GFt/92ud//YZvK/0yFvP9HerL/VIzA/1mazf9RmM7/bKrM/22v0P+q6fv/sev7/36+3P9YmMz/
Zoij/46do/+dqav/m6er/5+6wf+o5vH/peLy/4nE3f+W2Oz/ndrv/4G/1f+x6PX/ntXk/1qUuv+O
yd//jcbV/7fr/P+a0uj/bqnI/7Hr+f+Oxt7/aKjQ/4K/3/9ejbz/otju/5vW6v+y6/n/bq3S/4TG
4v90p8b/ZZzN/0yCuP99vt//nNjq/0yBsf+AwOL/aarS/1OUz/9Qgrr/VIy9/1ycx/9Umc3/X5rC
/26w0f+q6fv/sO36/4rJ4/9YmdD/XIOm/42ao/+cp6n/n6qt/6XFzf+s6fX/puXy/4bC2v+X1ur/
n9vv/4fF2v+x6PT/n9Xl/2CYvv+VyuD/pdvo/7vt+v+i2Or/bajF/7js+/+j1ub/cLTY/47L5f9i
k73/r+j3/63n9v+17Pn/ebnX/4TH4P9uobv/drDX/1may/+Pz+j/pN3v/0R6pf+IyeX/eLnY/06Y
z/9Qh77/VY+7/16ewf9qrNj/Uo+9/22v0v+t6f3/tPD6/5jU6P9SmM7/V4Kp/4ubo/+dqav/nqmt
/6zP1/+07fn/puTw/4TA2f+W1On/otzv/4K+1f+n3ez/nNLg/2+myf+Ov9b/tuz5/8Dy/P+u5PP/
bKfE/7ru+/+55/H/eLrZ/5/Z7/9ekbf/suv6/7Pt+v+67/v/hMPd/4nM4/95sMb/hcDf/12fyv+h
3vL/qeLy/0yGr/+W1ev/jMXf/0+azv9Kh7z/WZO9/2WkxP91t9v/T4y8/2yt0f+s6Pr/s+/5/6fc
7P9Umc3/VIOt/4mapP+apqj/maOp/7Ta4f+88Pr/r+n2/4O91/+LyuL/pd7x/3mxzP+XzN7/ms/a
/4S61v+KutP/t+37/8Dy/f+17Pn/a6jB/7rv+f/N9fv/g7/Z/7Lq+f9roL//te38/7jv/P+98fv/
jMrh/47P5v9+u8z/mtPn/2alyP+17/v/rObz/1KQtv+s5fb/oNHn/1Oazf9Ti77/YpjA/16duv92
udr/TIm4/22t0P+c2+r/te/6/7rl8v9Zmsz/ToOx/4qZp/+bpqr/kJ2j/7vh6f/A7/n/te37/4S+
2f98u9b/p9/y/2egwP+EutD/odTe/5LI3/+Ov9f/t+37/77w/P+37fn/bqvB/7rv+f/S+Pz/l8/j
/7fv+v96scr/tuz7/7nu/P++8fv/ktDl/5LT6f+DwM3/rOPy/3m10P+78fv/sen1/12bvv+77/z/
sNrt/1eazP9ViLr/dKnN/1aVtP91udr/S4m5/2+w0f+Ozd7/tez5/8jr9f9dm8n/SIGy/4mZqv+b
paz/jZyj/8Pn8P/E8fr/tu38/4bC2/9zstL/qeL1/1GOtv98tNH/otLe/6nf8f+Bs8n/ue38/73v
/P+67vr/eLHG/7ju+f/L9vr/pt3r/7jw+/+Lw9f/tev4/7zu+/+98Pz/l9Xo/5fX6/+Vzdn/ter3
/5DI2f++8fv/ptvn/3q00P/G8/v/vOTz/1ycxv9Me6b/hb3Z/1STuP9wtNn/Som7/3672f97u9H/
sur4/83v+f9gnMT/R4S0/4CWp/+apKv/j5yh/8jq8f/G8fn/uO76/43I3v9zs9f/mtbt/02NuP9p
o8j/o9Le/7nt+v99rsP/ue35/8Dw+/+67fn/h8HU/6ng7f/D8/v/tuv4/7jv+v+k2+v/r+by/7zv
/P+88Pv/ndnq/6Dd7v+e1+T/tun2/67h8P++8Pv/l8zZ/5bQ4//K9fv/wOv3/3GsyP9ii6j/hr/X
/1qYv/9nq9b/UY+//5LK4P9mp8j/ser6/8jw+f9vp8v/Toq5/3qQo/+cpa3/kZ2g/8Lj6P/L9fr/
u/D6/5PM4P9usNf/g8Hf/0yPuv9dl8L/odHc/73v+P+Ht8r/u+/4/8Xz/P+87/v/ot3u/43F1P+8
7/3/u+/8/7rw+v+17Pj/tez4/7zv/P+88Pv/ot3s/6rm9P+v6ff/uu/6/73v/P++8Pv/j8TS/6/o
9f/M9Pr/we33/4a/0f98rsX/kczc/2Wkyf9Wm8v/XJjH/5nO4P9doMr/tO36/8Lw+f99stL/T4u5
/3eNo/+cpa3/mqap/7HQ1v/S9vz/ve/6/4rG1v9nps3/aqnU/1aXy/9Sjrn/rN7s/6/g5/+r3ez/
o9jf/8z1+v++8Pr/r+z4/4O9yf+/7fr/uu38/7nu+/+z7vz/te38/7vu/v+57f3/rOb1/7Dt+/+y
7fv/t/L8/7vw/P+77v3/oNPg/7Lq+v/G8/v/vu34/5vR3v+QxNT/mc/c/2+pzv9FiLz/Y6PN/43E
2f9hp9T/tO/7/7zs+f+DutX/UYq7/3qPpf+ao6v/nKms/6bCyv/R9fz/wPD7/6Pc6/9Xlr//VpjQ
/1SZ0/8+fan/ten5/6DS2v++7/r/sebx/8z2/P/B8fv/s+37/4bBzf+98Pv/ue37/7nu+/+z7vz/
tu79/7vu/v+57f3/tO38/7Ht/P+y7fz/t/L9/7nv/P+57vz/qd7r/7ft/P/C8fr/ve36/7Dk8f+s
4e3/mM7Z/3Ov0/9Chbn/ZKfT/3Sv0f9ustv/te/7/7js+P+Du9j/UoWz/4SVp/+cpa3/mqiq/5+4
wP/N8/r/w/H9/7nu+v9clLb/VJjR/0+Z0/88fav/quHz/5zQ2P/C8vn/uO37/8Tz/P+/8vr/tez6
/5/a5v+p3un/tez6/7ju+/+z7v3/te38/7rt/f+57fz/tO38/7Ht+/+y7fz/tfD8/7Xu/P+07fv/
tu36/7nt/P+/8Pv/ve7+/73t+/+27fb/lsvV/3Wy1v9Dhrr/XKHV/1ydzP9+weD/t+/8/7ft+v98
tNP/VoSt/4iUov+cpq3/laWr/4+lq//J8fj/w+/7/7rt+/9+tM3/V5nN/02X0v88gLD/grnL/6LU
4P+35+3/uO38/7vv/P+97/z/tO37/7Pu+v+c097/tOz7/7ft/P+17Pv/te38/7nt/f+47fz/s+39
/7Ht/P+y7Pz/tO39/7Tu/P+z7vz/su37/7jt/P+97/3/ve7+/7vu+/+h1d//ruLv/3e11v9ChLj/
TpjQ/1Oazf+Jxt3/ue/9/6/q+f9sp8r/X4Ki/4eWn/+apKv/lKSr/4qdov+93+f/xe/7/7ru+/+j
2+v/VJO6/0+V0P9HjcL/XZKo/6nd7f+e0dr/ue38/7bs+/+57Pz/s+38/7Tu+/+27vr/tO37/7bt
/P+17Pz/tO38/7fs/P+27Pv/s+z8/7Hu/P+z7P3/tOz9/7Xu/f+y7vz/su78/7ft/P+67f3/ue38
/7ft+f+Xy9T/tez6/2upyf9Rk8f/TJjS/1CVwf+q4vL/t+z8/5/a7f9UjrL/dI6j/4eXnv+Zo6r/
l6Ws/5elq/+huMH/xu35/7ju/P+y7Pn/cKvC/1qbyP9Wms3/Xomr/57L4P+k2OD/suby/7Xt/P+4
7v7/s+38/7bv/P+07fz/s+38/7Pt/P+y7fz/tO38/7jt/f+37fz/s+z8/7Hu/P+z7P3/tO39/7Xu
/f+y7vz/su/9/7ft/f+47v3/te37/7Pq9P+bztf/uuv5/2mev/9Zmc7/UZjO/2uqyf+z6/j/tev5
/5fP5v9UhaP/f5ag/4WVnf+Yoqr/maSs/5ikqv+MnKX/xer2/7bs/P+z7/v/rOX0/2Kat/9XkLn/
SGSR/22Jrf/D7PX/mczW/7Xt+v+27v3/tO38/7bu/f+y7Pz/tO39/7Ht/P+x7Pv/su37/7bu+/+2
7v3/sez8/7Ht+/+z7Pz/tO39/7Tt/P+z7vz/su79/7bt/f+17vz/s+77/5nP2P+u2uL/osLV/2KI
qv9emcv/U5TA/5bR5f+z7Pv/tOz6/4u+1P9liJ3/fpSc/4SUnP+Yoar/maSr/5ikqv+Zpa3/or7G
/7rt+f+z7v3/su38/63k9v9yn7r/Vl+f/yw2fP+Yssr/suHr/6Xa5P+17fv/tez7/7Pu/P+y7fz/
te39/7Hu/f+17fz/tO38/7Pt/P+y7v3/sO37/7Lt/P+y7Pv/sez8/7Pu/f+z7v3/s+79/7Pu/f+1
7Pv/se35/6TN1v+XsL3/R1SD/2Bynf9YhK3/gb/b/6/o+f+06/v/tez6/3efsP9/l6X/gZSe/4OV
nP+Yoa7/lqSq/5ejqf+apKr/jp6j/7jf6P+27vn/s+76/53Z5P9qlK7/UE+w/zAum/9FTpL/tdjp
/7vr9v+z7vr/su77/7Ht+/+z7vv/te77/7Lw/P+17vz/tOz9/7Tt/v+z7fv/tO37/7Pt+/+z7fz/
su38/7Pu/v+07/7/su39/7Lt/P+z7fz/tu36/6S+yv9TWoj/MS6M/2FhrP93lbn/dq/K/6Ld8P+0
7fz/otHc/3GNnP+ElKP/gpOe/4GTm/+Hj5//mKis/5mlq/+apqn/maan/4WmrP+67vj/tO/5/7Hy
9/94obr/V1TH/0E7uv9FPbD/d4uu/7Pf7P+x8ff/sPH5/7Hw+f+z8Pn/tu/5/7Px+v+28Pr/tvL6
/7bz+/+38fr/uPD6/7Xv+f+y8Pn/s/D6/7Pw+/+z8Pv/s+/7/7Lt+/+v6vn/k8TQ/36OpP9FSqP/
ODe0/1tTwP+gudn/nNbp/6Dd7f+v6fb/dpup/4aYpP+Jk6L/g5Of/4KVnP8AAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA='''
wrong_picture = b'''\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\xa1\x00\x00\x00Q\x01\x03\x00\x00\x00\x80\rT\xec\x00\x00\x00\x06PLTE"""\xff\xff\xff^\x87 1\x00\x00\x01\xacIDATx^\xed\xd0/o\xdb@\x18\x06\xf0\xd7Q\x96\xb9\xcc6\xacn\xd5\xe5@j\x10\x90T\x01\x05\xd3t\x93n\xcb\x81HUY`@A\xa0\x9d\x91\x8d\x9d\x07\x96;\xb2\xe8\x86ZRU%\xa5\xfb\nEI\x99?\x82S4\x98\xb1\x90I\xbb\x9c\x9b\xbf3\x19h\xb7I{$\x93\x9f^=:?\xf0\xf7\xc6\xf9\x01@\x7f\xe5\xaa\x81\x02\xedeo\xce\xa34\x93\xf7\xf8\xf8f\xad\xda{{\xa6\x9a\x9e\n0\x9b\x88\x95\xfa\x1ec{\xbew\x1a\xe0\xb2\xdc\xd0\x19c\x1f\xfc\x99\xd1\x97\xa3\r\x05\xc6\x94\x0fF\x99\x84\xad\x86\x8b\xa6W\rpg\xa3\xc1\xcb\x18\xeb\xa7\x19\x9ef\xad!l\xc7\x03\\\xf0\x87\x19Px\x84p\x80\x92\x05\n\xae\xb3R\xbaV\xb0zS\xd1\x08}\xfb\x9a\xee\x1fGQ\x1de\x83\xf0\x9d0:Q\x9a\x10~\xd7\xa81)\x8f\x08U\\\x81\x89\x94\x9a`\xae<\xc2\xa4 \x0bM\x16:\x92\xfa\x15\xb2:\x8f\x8c\xceelo]\x8dKV\x85k4\xe1{Vm\xafj\x98\x06IV\xbd\xc3\xca\x08\xa1\xbeL\x0f\xcc\x1b\x08\xea\r\xc28\x9fS\xe4\xa3\xedD\xe4\xa3=M\x1c\xfb\xe5\xf1\x81\xd2\xa5\xaf\xd5Yj\xfc\x1a=\x1b:\xa8\xde\x8a\xae\xee\x0f}\xd4m[U\t\xa9\xf0\x84\x1cu\xe4m\x10jr\xc6\x85U\x07\x97\x8d.\x86\xf4\xa9.\xb1\xa5\xa2\\\xe7\xe2{[\x1f\xb0\x93\x07-\xe5*\x12\x9fk\xc28\xe4J\xacvd\xd2P\xba\xf6\xd0\x1b\x9b\x86\xb6\x83H+\x12\xe9\'\xbd\xdfmo\xadW\x86\xa2\xbc\x87?\x9d\xff\x11\xbfq\xfby|=\x1d\xbf\x10;\xaa\xc2\xeb\x8f\xe1\x17Z\xa0n\x81\x16\xde\x1e^\xaaq\xb0\xab\xe0\x16\xbe\xed9\xfc\xf3\xf9\t\x93\x80\x88\xce\xd7u"\xb2\x00\x00\x00\x00IEND\xaeB`\x82'''
icondata= base64.b64decode(icon)
tempFile= "icon.ico"
iconfile= open(tempFile,"wb")
iconfile.write(icondata)
iconfile.close()
def closs() :
    os._exit(0)
def selectPath():
    path_ = askdirectory()
    path.set(path_)
def changepage ():
    text.insert(END,'開始下載\n')
    text.see(END)
    q = int(e.get())
    #e = 結束
    b = int(w.get())
    #w = 開始
    while q+1>b :
        findurl('https://disp.cc/b/Beauty?pn='+str(b)+'&init=0')
        for each in urls :
            Download('https://disp.cc/b/'+each)
            text.insert(END,'進入下一篇文章\n')
            text.see(END)
        b +=20
    messagebox.showinfo('Notice','已下載完畢')
    
    
def findurl(a) :
    req = r.Request(a)
    req.add_header('User-Agent','Mozilla/5.0 (X11; NetBSD) AppleWebKit/547.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36')
    response = r.urlopen(req)
    f1 = response.read().decode("UTF-8")
    soup = BeautifulSoup(f1,"html.parser")
    a = str(soup.find_all('a'))
    global urls
    urls = re.findall('62-\w\w\w\w',a)
def Download (x) :
    final = []
    a = None
    req = r.Request(x)
    req.add_header('User-Agent','Mozilla/5.0 (X11; NetBSD) AppleWebKit/547.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36')
    response = r.urlopen(req)
    f1 = response.read().decode("UTF-8")
    soup = BeautifulSoup(f1,"html.parser")
    a = str(soup.find_all('a'))
    target = re.findall('https://i.imgur.com/\w\w\w\w\w\w\w',a)
    if target ==[] :
        target = re.findall('http://imgur.com/\w\w\w\w\w\w\w',a)
    for each in target :
        if a == each :
            continue
        else :
            final.append(each)
            a = each
    for each in final :
        global count_
        response = r.urlopen(each+'.jpg')
        image = response.read()
        if image == wrong_picture :
            continue
        name = each.replace('/','0')
        name = name.replace('.','1')
        name = name.replace(':','2')
        with open(path.get()+'/'+name+'.jpg','wb') as f:
            f.write(image)
        count_ +=1
        text.insert(END,str(each)+'.jpg已下载\n')
        text.see(END)
        count.set(count_)
        
t= threading.Thread(target = changepage)
root = Tk()
count = IntVar()
count_ = 0
root.geometry('560x200')
root.title('ptt爬蟲')
root.wm_iconbitmap(tempFile)
path = StringVar()
Label(root,text = "目標路徑:").grid  (column=0,row=0)
Entry(root, textvariable = path).grid  (column=1,row=0)
Button(root, text = "路徑選擇", command = selectPath).grid  (column=2,row=0)
Label(root,text = "開始頁數:").grid  (column=0,row=1)
w = Entry(root)
w.insert(END, '15001')
w.grid  (column=1,row=1)
Label(root,text = "結束頁數:").grid(column=0,row=2)
e = Entry(root)
e.insert(END, '15061')
e.grid(column=1,row=2)
b = Button(root, text="開始", command=t.start)
b.grid  (column=0,row=3)
c = Button(root, text="結束", command=closs)
c.grid  (column=1,row=3)
Label(root,text = "目前已儲存個數:").grid(column=0,row=4)
Label(root,textvariable=count,fg = 'red').grid  (column=1,row=4)
text=tkst.ScrolledText(root,fg='blue', width  = 38, height = 15)
text.grid(column=5,row=0,rowspan=8)
os.remove(tempFile)
root.mainloop()
