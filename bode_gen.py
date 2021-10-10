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

ksi_z = 0.1
omega_z = 200 * 2 * np.pi
ksi_p = 0.8
omega_p = 200 * 2 * np.pi

tf_1 = ctrl.tf([1, 2 * ksi_z * omega_z, omega_z ** 2], [1, 2 * ksi_p * omega_p, omega_p ** 2])
tf_sg = sg.TransferFunction([1, 2 * ksi_z * omega_z, omega_z ** 2], [1, 2 * ksi_p * omega_p, omega_p ** 2])
# tf_1 = ctrl.tf([1], [1, 2 * ksi_p * omega_p, omega_p ^ 2])
# tf_1 = sg.TransferFunction([1, 1, 1], [1, 2, 1])
# mag, phase, w = ctrl.bode_plot(tf_1, dB=True, margins=True, wrap_phase=False)
w = range(1, round(2000. * 2. * np.pi))
mag, phase, w = ctrl.bode_plot(tf_1, omega=w, dB=True, Hz=True, margins=False, wrap_phase=False)

s = ctrl.tf([1, 0], [1])
tf_2 = tf_1 / s
print(tf_2)


#================== selfdefine freq respone func ============================#
def freqrespon(num, den, omega):
    order = len(num)
    magnitude = []
    phase = []
    freqHz = []
    for w_index in range(len(omega)):
        _num = 0
        _den = 0
        for i in range(order):
            _num += num[order - 1 - i] * (1j * omega[w_index]) ** i
        for k in range(order):
            _den += den[order - 1 - k] * (1j * omega[w_index]) ** k
        final = _num / _den
        magnitude += [np.abs(final)]
        phase += [np.angle(final)]
        freqHz += [omega[w_index] / 2 / np.pi]
    return magnitude, phase, freqHz


w = range(1, round(2000 * 2 * np.pi))
magnitude, phase, freqHz = freqrespon([1, 2 * ksi_z * omega_z, omega_z ** 2], [1, 2 * ksi_p * omega_p, omega_p ** 2], w)
plt.figure()
plt.semilogx(freqHz, [20 * np.log10(i) for i in magnitude])
plt.title("freqrespon mag")
plt.figure()
plt.semilogx(freqHz, [(180 / np.pi) * i for i in phase])
plt.title("freqrespon phase")
plt.show()

w = range(1, round(1000))
mag1, phase1, w1 = ctrl.freqresp(tf_1, w)
plt.figure()
# plt.plot(w,mag)
plt.semilogx(w1, 20 * np.log10(mag1))
plt.figure()
plt.semilogx(w1, (180 / np.pi) * phase1)
plt.title("tf_1_freq")
plt.show()

print(tf_1.num[0][0], tf_1.den[0][0])

#========================= end ===============================#
