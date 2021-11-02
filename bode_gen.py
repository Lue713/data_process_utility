import numpy as np
import matplotlib.pyplot as plt
from scipy import signal as sg
import control as ctrl

#
# s = sg.TransferFunction([1, 0], [1])
# # tf_2 = s/(s*s + s + 2)
#
#
# tf_1 = sg.TransferFunction([1], [1, 1, 2])
# print(tf_1)
# omega, H = sg.freqresp(tf_1, 1000)
# freq = omega/2/np.pi
# plt.figure()
# plt.plot(H.real, H.imag, "b")
# # plt.plot(H.real, -H.imag, "r")
# plt.show()
#
#
# s = ctrl.TransferFunction([1], [1, 0, 0])
# w, mag, phase = ctrl.bode(s, dB = True)
#
# s = sg.lti([1], [1, 0, 0])
# w, mag, phase = sg.lti.bode(s);
# plt.figure()
# plt.semilogx(w, mag)  # Bode magnitude plot
# plt.figure()
# plt.semilogx(w, phase)  # Bode phase plot
# plt.show()
# # w, h = ctrl.freqresp(s)


# ****************************************************************************
# ksi_z = 0.1
# omega_z = 200 * 2 * np.pi
# ksi_p = 0.8
# omega_p = 200 * 2 * np.pi
# Ts = 0.0001
#
# # tf_1 = ctrl.tf([1, 2 * ksi_z * omega_z, omega_z ** 2], [1, 2 * ksi_p * omega_p, omega_p ** 2])
# tf_1 = ctrl.tf([1, 2 * ksi_z * omega_z, omega_z ** 2], [1, 2 * ksi_p * omega_p, omega_p ** 2])
# print("tf_1 = ", tf_1)
# tfd_1 = tf_1.sample(Ts, method='bilinear', prewarp_frequency=10)
# print("tfd_1 = ", tfd_1)
# # tf_sg = sg.TransferFunction([1, 2 * ksi_z * omega_z, omega_z ** 2], [1, 2 * ksi_p * omega_p, omega_p ** 2])
# # tf_1 = ctrl.tf([1], [1, 2 * ksi_p * omega_p, omega_p ^ 2])
# # tf_1 = sg.TransferFunction([1, 1, 1], [1, 2, 1])
# # mag, phase, w = ctrl.bode_plot(tf_1, dB=True, margins=True, wrap_phase=False)
# w = range(1, round(2000. * 2. * np.pi))
# plt.figure()
# mag, phase, w = ctrl.bode_plot(tf_1, omega=w, dB=True, Hz=True, margins=False, wrap_phase=False)
# plt.show()
# w = range(1, round(2000. * 2. * np.pi))
# plt.figure()
# mag_d, phase_d, w = ctrl.bode_plot(tfd_1, omega=w, dB=True, Hz=True, margins=False, wrap_phase=False)
# plt.show()
#
# s = ctrl.tf("s")
# tf_2 = (s+1)/s
# print("tf_2 = ", tf_2, s)
# ****************************************************************************


# https://github.com/python-control/python-control/issues/657
# https://trepo.tuni.fi/bitstream/handle/123456789/26690/Heinanen.pdf?sequence=4&isAllowed=y
# https://aiecp.files.wordpress.com/2012/07/1-0-1-k-j-astrom-pid-controllers-theory-design-and-tuning-2ed.pdf
s = ctrl.tf("s")


def pidtune(GH, BW, PM):
    '''Evaluate a PID control used on power eletronics.

    Parameters:
        Open loop plant*sensor transfer function.
        Bandwidth in rad/s.
        Phase margin in degrees.
    '''
    from math import sqrt, tan, radians
    from numpy import angle
    # Evaluate the plant transfer function on the intended bandwidth frequency.
    evaluated_BW = GH(1j * BW)
    evaluation_gain = abs(evaluated_BW)
    evaluation_angle = angle(evaluated_BW)
    # Evaluate the gain and margin phase that the control must apply.
    pi_gain = 1 / evaluation_gain
    pi_phase = radians(PM) - (np.pi - evaluation_angle)
    # Convert the gain and margin to control gain parameters.
    Kp_Ki = 1 / BW * tan(pi_phase + np.pi / 2)
    Ki = pi_gain / sqrt(1 / BW ** 2 + Kp_Ki ** 2)
    Kp = Ki * Kp_Ki
    Kd = 0
    return Kp + Ki / s + Kd * s


alpha = 0.1
k = 0.5
GHi = k / (s * (s + alpha))
Ci_BW = 25

GH = GHi
BW = 2 * np.pi * Ci_BW
PM = 40
print(GH, BW, PM)

from scipy.optimize import minimize


def optimize_fnc(x):
    PID = x[0] + x[1] / s + (x[2] * s)
    gm, pm, wg, wp = ctrl.margin(GH * PID)
    return (pm - PM) ** 2 + (BW - wp) ** 2


r = minimize(optimize_fnc, [0, 0, 0], method='nelder-mead', options={'xtol': 1e-8, 'disp': True})
print('Kp, Ki, Kd = ', r.x)
PID_opt = r.x[0] + r.x[1] / s + (r.x[2] * s)
OL_opt = GH * PID_opt
CL_opt = OL_opt/(1+OL_opt)

w = range(1, round(2000. * 2. * np.pi))
ctrl.bode_plot(OL_opt, omega=w, dB=True, Hz=True, margins=False, wrap_phase=False)
plt.show()
ctrl.bode_plot(CL_opt, omega=w, dB=True, Hz=True, margins=False, wrap_phase=False)
plt.show()

# def optimize_fnc(x):
#     PID = x[0] + x[1] / s
#     gm, pm, wg, wp = ctrl.margin(GH * PID)
#     return (pm - PM) ** 2 + (BW - wp) ** 2
#
# r = minimize(optimize_fnc, [0, 0], method='nelder-mead', options={'xtol': 1e-8, 'disp': True})
# print('Kp, Ki = ', r.x)




# ================== selfdefine freq respone func ============================#
# def freqrespon(num, den, omega):
#     order = len(num)
#     magnitude = []
#     phase = []
#     freqHz = []
#     for w_index in range(len(omega)):
#         _num = 0
#         _den = 0
#         for i in range(order):
#             _num += num[order - 1 - i] * (1j * omega[w_index]) ** i
#         for k in range(order):
#             _den += den[order - 1 - k] * (1j * omega[w_index]) ** k
#         final = _num / _den
#         magnitude += [np.abs(final)]
#         phase += [np.angle(final)]
#         freqHz += [omega[w_index] / 2 / np.pi]
#     return magnitude, phase, freqHz
#
#
# w = range(1, round(2000 * 2 * np.pi))
# magnitude, phase, freqHz = freqrespon([1, 2 * ksi_z * omega_z, omega_z ** 2], [1, 2 * ksi_p * omega_p, omega_p ** 2], w)
# plt.figure()
# plt.semilogx(freqHz, [20 * np.log10(i) for i in magnitude])
# plt.title("freqrespon mag")
# plt.figure()
# plt.semilogx(freqHz, [(180 / np.pi) * i for i in phase])
# plt.title("freqrespon phase")
#
# w = range(1, round(1000))
# mag1, phase1, w1 = ctrl.freqresp(tf_1, w)
# plt.figure()
# # plt.plot(w,mag)
# plt.semilogx(w1, 20 * np.log10(mag1))
# plt.figure()
# plt.semilogx(w1, (180 / np.pi) * phase1)
# plt.title("tf_1_freq")
# plt.show()
#
# plt.show()
# print(tf_1.num[0][0], tf_1.den[0][0])

# ========================= end ===============================#
