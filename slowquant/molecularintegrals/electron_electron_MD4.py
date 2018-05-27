import numpy as np
from numpy import exp
from numba import jit, float64
from slowquant.molecularintegrals.utility import ERI_expansion_coeff_sum, Contraction_two_electron
from slowquant.molecularintegrals.expansion_coefficients import *
from slowquant.molecularintegrals.hermite_integral import *


@jit(float64[:](float64[:], float64[:], float64[:], float64[:], float64[:], float64[:], float64[:], float64[:], float64[:], float64[:], float64[:], float64[:], float64[:,:,:,:,:], float64[:,:,:,:], float64[:,:,:,:], float64[:,:,:,:], float64[:], float64[:,:,:]), nopython=True, cache=True)
def electron_electron_integral_0_0_0_0_MD4(Coord_1, Coord_2, Coord_3, Coord_4, gauss_exp_1, gauss_exp_2, gauss_exp_3, gauss_exp_4, Contra_coeffs_1, Contra_coeffs_2, Contra_coeffs_3, Contra_coeffs_4, primitives_buffer, E_buff_1, E_buff_2, R_buffer, output_buffer, Norm_array):
    number_primitive_1 = gauss_exp_1.shape[0]
    number_primitive_2 = gauss_exp_2.shape[0]
    number_primitive_3 = gauss_exp_3.shape[0]
    number_primitive_4 = gauss_exp_4.shape[0]
    XAB_left = Coord_1 - Coord_2
    XAB_right = Coord_3 - Coord_4
    for i in range(0, number_primitive_1):
        gauss_exp_1_left = gauss_exp_1[i]
        for j in range(0, number_primitive_2):
            gauss_exp_2_left = gauss_exp_2[j]
            p_left = gauss_exp_1_left + gauss_exp_2_left
            q_left = gauss_exp_1_left * gauss_exp_2_left / p_left
            P_left = (gauss_exp_1_left*Coord_1 + gauss_exp_2_left*Coord_2) / p_left
            XPA_left = P_left - Coord_1
            XPB_left = P_left - Coord_2
            p12_left = 1.0/(2.0*p_left)
            E_buff_1 = E_0_0_0(q_left, p12_left, XAB_left, XPA_left, XPB_left, E_buff_1)
            for k in range(0, number_primitive_3):
                gauss_exp_1_right = gauss_exp_3[k]
                for l in range(0, number_primitive_4):
                    gauss_exp_2_right = gauss_exp_4[l]
                    p_right = gauss_exp_1_right + gauss_exp_2_right
                    q_right = gauss_exp_1_right * gauss_exp_2_right / p_right
                    P_right = (gauss_exp_1_right*Coord_3 + gauss_exp_2_right*Coord_4) / p_right
                    alpha = p_left*p_right/(p_left+p_right)
                    XPC, YPC, ZPC = P_left - P_right
                    RPC = ((XPC)**2+(YPC)**2+(ZPC)**2)**0.5
                    E_buff_2[0,0,0,:] = exp(-q_right*XAB_right*XAB_right)
                    R_array = R_0_0_0_0(alpha, XPC, YPC, ZPC, RPC, R_buffer)
                    counter = 0
                    primitives_buffer[i,j,k,l,counter] = ERI_expansion_coeff_sum(E_buff_1[0,0,:,0],E_buff_1[0,0,:,1],E_buff_1[0,0,:,2],E_buff_2[0,0,:,0],E_buff_2[0,0,:,1],E_buff_2[0,0,:,2],R_array,1,1,1,1,1,1)
                    counter += 1
                    primitives_buffer[i,j,k,l,:1] = 1.0/(p_left*p_right*(p_left+p_right)**0.5)*primitives_buffer[i,j,k,l,:1]
    for i in range(0, 1):
        output_buffer[i] = Contraction_two_electron(primitives_buffer[:,:,:,:,i], Contra_coeffs_1, Contra_coeffs_2, Contra_coeffs_3, Contra_coeffs_4)*9.027033336764104
    return output_buffer


@jit(float64[:](float64[:], float64[:], float64[:], float64[:], float64[:], float64[:], float64[:], float64[:], float64[:], float64[:], float64[:], float64[:], float64[:,:,:,:,:], float64[:,:,:,:], float64[:,:,:,:], float64[:,:,:,:], float64[:], float64[:,:,:]), nopython=True, cache=True)
def electron_electron_integral_1_0_0_0_MD4(Coord_1, Coord_2, Coord_3, Coord_4, gauss_exp_1, gauss_exp_2, gauss_exp_3, gauss_exp_4, Contra_coeffs_1, Contra_coeffs_2, Contra_coeffs_3, Contra_coeffs_4, primitives_buffer, E_buff_1, E_buff_2, R_buffer, output_buffer, Norm_array):
    number_primitive_1 = gauss_exp_1.shape[0]
    number_primitive_2 = gauss_exp_2.shape[0]
    number_primitive_3 = gauss_exp_3.shape[0]
    number_primitive_4 = gauss_exp_4.shape[0]
    XAB_left = Coord_1 - Coord_2
    XAB_right = Coord_3 - Coord_4
    for i in range(0, number_primitive_1):
        gauss_exp_1_left = gauss_exp_1[i]
        for j in range(0, number_primitive_2):
            gauss_exp_2_left = gauss_exp_2[j]
            p_left = gauss_exp_1_left + gauss_exp_2_left
            q_left = gauss_exp_1_left * gauss_exp_2_left / p_left
            P_left = (gauss_exp_1_left*Coord_1 + gauss_exp_2_left*Coord_2) / p_left
            XPA_left = P_left - Coord_1
            XPB_left = P_left - Coord_2
            p12_left = 1.0/(2.0*p_left)
            E_buff_1 = E_1_0_1(q_left, p12_left, XAB_left, XPA_left, XPB_left, E_buff_1)
            for k in range(0, number_primitive_3):
                gauss_exp_1_right = gauss_exp_3[k]
                for l in range(0, number_primitive_4):
                    gauss_exp_2_right = gauss_exp_4[l]
                    p_right = gauss_exp_1_right + gauss_exp_2_right
                    q_right = gauss_exp_1_right * gauss_exp_2_right / p_right
                    P_right = (gauss_exp_1_right*Coord_3 + gauss_exp_2_right*Coord_4) / p_right
                    alpha = p_left*p_right/(p_left+p_right)
                    XPC, YPC, ZPC = P_left - P_right
                    RPC = ((XPC)**2+(YPC)**2+(ZPC)**2)**0.5
                    E_buff_2[0,0,0,:] = exp(-q_right*XAB_right*XAB_right)
                    R_array = R_1_0_0_0(alpha, XPC, YPC, ZPC, RPC, R_buffer)
                    counter = 0
                    primitives_buffer[i,j,k,l,:3] = 0.0
                    for x1 in range(1, -1, -1):
                        for y1 in range(1-x1, -1, -1):
                            for z1 in range(1-x1-y1, 0-x1-y1, -1):
                                for t in range(0, x1+1):
                                    for u in range(0, y1+1):
                                        for v in range(0, z1+1):
                                            primitives_buffer[i,j,k,l,counter] += E_buff_1[x1,0,t,0]*E_buff_1[y1,0,u,1]*E_buff_1[z1,0,v,2]*R_array[t,u,v]

                                counter += 1
                    primitives_buffer[i,j,k,l,:3] = 1.0/(p_left*p_right*(p_left+p_right)**0.5)*primitives_buffer[i,j,k,l,:3]*E_buff_2[0,0,0,0]*E_buff_2[0,0,0,1]*E_buff_2[0,0,0,2]
    for i in range(0, 3):
        output_buffer[i] = Contraction_two_electron(primitives_buffer[:,:,:,:,i], Contra_coeffs_1, Contra_coeffs_2, Contra_coeffs_3, Contra_coeffs_4)*18.054066673528208
    return output_buffer


@jit(float64[:](float64[:], float64[:], float64[:], float64[:], float64[:], float64[:], float64[:], float64[:], float64[:], float64[:], float64[:], float64[:], float64[:,:,:,:,:], float64[:,:,:,:], float64[:,:,:,:], float64[:,:,:,:], float64[:], float64[:,:,:]), nopython=True, cache=True)
def electron_electron_integral_1_0_1_0_MD4(Coord_1, Coord_2, Coord_3, Coord_4, gauss_exp_1, gauss_exp_2, gauss_exp_3, gauss_exp_4, Contra_coeffs_1, Contra_coeffs_2, Contra_coeffs_3, Contra_coeffs_4, primitives_buffer, E_buff_1, E_buff_2, R_buffer, output_buffer, Norm_array):
    number_primitive_1 = gauss_exp_1.shape[0]
    number_primitive_2 = gauss_exp_2.shape[0]
    number_primitive_3 = gauss_exp_3.shape[0]
    number_primitive_4 = gauss_exp_4.shape[0]
    XAB_left = Coord_1 - Coord_2
    XAB_right = Coord_3 - Coord_4
    for i in range(0, number_primitive_1):
        gauss_exp_1_left = gauss_exp_1[i]
        for j in range(0, number_primitive_2):
            gauss_exp_2_left = gauss_exp_2[j]
            p_left = gauss_exp_1_left + gauss_exp_2_left
            q_left = gauss_exp_1_left * gauss_exp_2_left / p_left
            P_left = (gauss_exp_1_left*Coord_1 + gauss_exp_2_left*Coord_2) / p_left
            XPA_left = P_left - Coord_1
            XPB_left = P_left - Coord_2
            p12_left = 1.0/(2.0*p_left)
            E_buff_1 = E_1_0_1(q_left, p12_left, XAB_left, XPA_left, XPB_left, E_buff_1)
            for k in range(0, number_primitive_3):
                gauss_exp_1_right = gauss_exp_3[k]
                for l in range(0, number_primitive_4):
                    gauss_exp_2_right = gauss_exp_4[l]
                    p_right = gauss_exp_1_right + gauss_exp_2_right
                    q_right = gauss_exp_1_right * gauss_exp_2_right / p_right
                    P_right = (gauss_exp_1_right*Coord_3 + gauss_exp_2_right*Coord_4) / p_right
                    alpha = p_left*p_right/(p_left+p_right)
                    XPC, YPC, ZPC = P_left - P_right
                    RPC = ((XPC)**2+(YPC)**2+(ZPC)**2)**0.5
                    XPA_right = P_right - Coord_3
                    XPB_right = P_right - Coord_4
                    p12_right = 1.0/(2.0*p_right)
                    E_buff_2 = E_1_0_1(q_right, p12_right, XAB_right, XPA_right, XPB_right, E_buff_2)
                    R_array = R_1_0_1_0(alpha, XPC, YPC, ZPC, RPC, R_buffer)
                    counter = 0
                    for x1 in range(1, -1, -1):
                        for y1 in range(1-x1, -1, -1):
                            for z1 in range(1-x1-y1, 0-x1-y1, -1):
                                for x3 in range(1, -1, -1):
                                    for y3 in range(1-x3, -1, -1):
                                        for z3 in range(1-x3-y3, 0-x3-y3, -1):
                                            primitives_buffer[i,j,k,l,counter] = ERI_expansion_coeff_sum(E_buff_1[x1,0,:,0],E_buff_1[y1,0,:,1],E_buff_1[z1,0,:,2],E_buff_2[x3,0,:,0],E_buff_2[y3,0,:,1],E_buff_2[z3,0,:,2],R_array,x1+1,y1+1,z1+1,x3+1,y3+1,z3+1)
                                            counter += 1
                    primitives_buffer[i,j,k,l,:9] = 1.0/(p_left*p_right*(p_left+p_right)**0.5)*primitives_buffer[i,j,k,l,:9]
    for i in range(0, 9):
        output_buffer[i] = Contraction_two_electron(primitives_buffer[:,:,:,:,i], Contra_coeffs_1, Contra_coeffs_2, Contra_coeffs_3, Contra_coeffs_4)*36.108133347056416
    return output_buffer


@jit(float64[:](float64[:], float64[:], float64[:], float64[:], float64[:], float64[:], float64[:], float64[:], float64[:], float64[:], float64[:], float64[:], float64[:,:,:,:,:], float64[:,:,:,:], float64[:,:,:,:], float64[:,:,:,:], float64[:], float64[:,:,:]), nopython=True, cache=True)
def electron_electron_integral_1_1_0_0_MD4(Coord_1, Coord_2, Coord_3, Coord_4, gauss_exp_1, gauss_exp_2, gauss_exp_3, gauss_exp_4, Contra_coeffs_1, Contra_coeffs_2, Contra_coeffs_3, Contra_coeffs_4, primitives_buffer, E_buff_1, E_buff_2, R_buffer, output_buffer, Norm_array):
    number_primitive_1 = gauss_exp_1.shape[0]
    number_primitive_2 = gauss_exp_2.shape[0]
    number_primitive_3 = gauss_exp_3.shape[0]
    number_primitive_4 = gauss_exp_4.shape[0]
    XAB_left = Coord_1 - Coord_2
    XAB_right = Coord_3 - Coord_4
    for i in range(0, number_primitive_1):
        gauss_exp_1_left = gauss_exp_1[i]
        for j in range(0, number_primitive_2):
            gauss_exp_2_left = gauss_exp_2[j]
            p_left = gauss_exp_1_left + gauss_exp_2_left
            q_left = gauss_exp_1_left * gauss_exp_2_left / p_left
            P_left = (gauss_exp_1_left*Coord_1 + gauss_exp_2_left*Coord_2) / p_left
            XPA_left = P_left - Coord_1
            XPB_left = P_left - Coord_2
            p12_left = 1.0/(2.0*p_left)
            E_buff_1 = E_1_1_2(q_left, p12_left, XAB_left, XPA_left, XPB_left, E_buff_1)
            for k in range(0, number_primitive_3):
                gauss_exp_1_right = gauss_exp_3[k]
                for l in range(0, number_primitive_4):
                    gauss_exp_2_right = gauss_exp_4[l]
                    p_right = gauss_exp_1_right + gauss_exp_2_right
                    q_right = gauss_exp_1_right * gauss_exp_2_right / p_right
                    P_right = (gauss_exp_1_right*Coord_3 + gauss_exp_2_right*Coord_4) / p_right
                    alpha = p_left*p_right/(p_left+p_right)
                    XPC, YPC, ZPC = P_left - P_right
                    RPC = ((XPC)**2+(YPC)**2+(ZPC)**2)**0.5
                    E_buff_2[0,0,0,:] = exp(-q_right*XAB_right*XAB_right)
                    R_array = R_1_1_0_0(alpha, XPC, YPC, ZPC, RPC, R_buffer)
                    counter = 0
                    primitives_buffer[i,j,k,l,:9] = 0.0
                    for x1 in range(1, -1, -1):
                        for y1 in range(1-x1, -1, -1):
                            for z1 in range(1-x1-y1, 0-x1-y1, -1):
                                for x2 in range(1, -1, -1):
                                    for y2 in range(1-x2, -1, -1):
                                        for z2 in range(1-x2-y2, 0-x2-y2, -1):
                                            for t in range(0, x1+x2+1):
                                                for u in range(0, y1+y2+1):
                                                    for v in range(0, z1+z2+1):
                                                        primitives_buffer[i,j,k,l,counter] += E_buff_1[x1,x2,t,0]*E_buff_1[y1,y2,u,1]*E_buff_1[z1,z2,v,2]*R_array[t,u,v]

                                            counter += 1
                    primitives_buffer[i,j,k,l,:9] = 1.0/(p_left*p_right*(p_left+p_right)**0.5)*primitives_buffer[i,j,k,l,:9]*E_buff_2[0,0,0,0]*E_buff_2[0,0,0,1]*E_buff_2[0,0,0,2]
    for i in range(0, 9):
        output_buffer[i] = Contraction_two_electron(primitives_buffer[:,:,:,:,i], Contra_coeffs_1, Contra_coeffs_2, Contra_coeffs_3, Contra_coeffs_4)*36.108133347056416
    return output_buffer


@jit(float64[:](float64[:], float64[:], float64[:], float64[:], float64[:], float64[:], float64[:], float64[:], float64[:], float64[:], float64[:], float64[:], float64[:,:,:,:,:], float64[:,:,:,:], float64[:,:,:,:], float64[:,:,:,:], float64[:], float64[:,:,:]), nopython=True, cache=True)
def electron_electron_integral_1_1_1_0_MD4(Coord_1, Coord_2, Coord_3, Coord_4, gauss_exp_1, gauss_exp_2, gauss_exp_3, gauss_exp_4, Contra_coeffs_1, Contra_coeffs_2, Contra_coeffs_3, Contra_coeffs_4, primitives_buffer, E_buff_1, E_buff_2, R_buffer, output_buffer, Norm_array):
    number_primitive_1 = gauss_exp_1.shape[0]
    number_primitive_2 = gauss_exp_2.shape[0]
    number_primitive_3 = gauss_exp_3.shape[0]
    number_primitive_4 = gauss_exp_4.shape[0]
    XAB_left = Coord_1 - Coord_2
    XAB_right = Coord_3 - Coord_4
    for i in range(0, number_primitive_1):
        gauss_exp_1_left = gauss_exp_1[i]
        for j in range(0, number_primitive_2):
            gauss_exp_2_left = gauss_exp_2[j]
            p_left = gauss_exp_1_left + gauss_exp_2_left
            q_left = gauss_exp_1_left * gauss_exp_2_left / p_left
            P_left = (gauss_exp_1_left*Coord_1 + gauss_exp_2_left*Coord_2) / p_left
            XPA_left = P_left - Coord_1
            XPB_left = P_left - Coord_2
            p12_left = 1.0/(2.0*p_left)
            E_buff_1 = E_1_1_2(q_left, p12_left, XAB_left, XPA_left, XPB_left, E_buff_1)
            for k in range(0, number_primitive_3):
                gauss_exp_1_right = gauss_exp_3[k]
                for l in range(0, number_primitive_4):
                    gauss_exp_2_right = gauss_exp_4[l]
                    p_right = gauss_exp_1_right + gauss_exp_2_right
                    q_right = gauss_exp_1_right * gauss_exp_2_right / p_right
                    P_right = (gauss_exp_1_right*Coord_3 + gauss_exp_2_right*Coord_4) / p_right
                    alpha = p_left*p_right/(p_left+p_right)
                    XPC, YPC, ZPC = P_left - P_right
                    RPC = ((XPC)**2+(YPC)**2+(ZPC)**2)**0.5
                    XPA_right = P_right - Coord_3
                    XPB_right = P_right - Coord_4
                    p12_right = 1.0/(2.0*p_right)
                    E_buff_2 = E_1_0_1(q_right, p12_right, XAB_right, XPA_right, XPB_right, E_buff_2)
                    R_array = R_1_1_1_0(alpha, XPC, YPC, ZPC, RPC, R_buffer)
                    counter = 0
                    for x1 in range(1, -1, -1):
                        for y1 in range(1-x1, -1, -1):
                            for z1 in range(1-x1-y1, 0-x1-y1, -1):
                                for x2 in range(1, -1, -1):
                                    for y2 in range(1-x2, -1, -1):
                                        for z2 in range(1-x2-y2, 0-x2-y2, -1):
                                            for x3 in range(1, -1, -1):
                                                for y3 in range(1-x3, -1, -1):
                                                    for z3 in range(1-x3-y3, 0-x3-y3, -1):
                                                        primitives_buffer[i,j,k,l,counter] = ERI_expansion_coeff_sum(E_buff_1[x1,x2,:,0],E_buff_1[y1,y2,:,1],E_buff_1[z1,z2,:,2],E_buff_2[x3,0,:,0],E_buff_2[y3,0,:,1],E_buff_2[z3,0,:,2],R_array,x1+x2+1,y1+y2+1,z1+z2+1,x3+1,y3+1,z3+1)
                                                        counter += 1
                    primitives_buffer[i,j,k,l,:27] = 1.0/(p_left*p_right*(p_left+p_right)**0.5)*primitives_buffer[i,j,k,l,:27]
    for i in range(0, 27):
        output_buffer[i] = Contraction_two_electron(primitives_buffer[:,:,:,:,i], Contra_coeffs_1, Contra_coeffs_2, Contra_coeffs_3, Contra_coeffs_4)*72.21626669411283
    return output_buffer


@jit(float64[:](float64[:], float64[:], float64[:], float64[:], float64[:], float64[:], float64[:], float64[:], float64[:], float64[:], float64[:], float64[:], float64[:,:,:,:,:], float64[:,:,:,:], float64[:,:,:,:], float64[:,:,:,:], float64[:], float64[:,:,:]), nopython=True, cache=True)
def electron_electron_integral_1_1_1_1_MD4(Coord_1, Coord_2, Coord_3, Coord_4, gauss_exp_1, gauss_exp_2, gauss_exp_3, gauss_exp_4, Contra_coeffs_1, Contra_coeffs_2, Contra_coeffs_3, Contra_coeffs_4, primitives_buffer, E_buff_1, E_buff_2, R_buffer, output_buffer, Norm_array):
    number_primitive_1 = gauss_exp_1.shape[0]
    number_primitive_2 = gauss_exp_2.shape[0]
    number_primitive_3 = gauss_exp_3.shape[0]
    number_primitive_4 = gauss_exp_4.shape[0]
    XAB_left = Coord_1 - Coord_2
    XAB_right = Coord_3 - Coord_4
    for i in range(0, number_primitive_1):
        gauss_exp_1_left = gauss_exp_1[i]
        for j in range(0, number_primitive_2):
            gauss_exp_2_left = gauss_exp_2[j]
            p_left = gauss_exp_1_left + gauss_exp_2_left
            q_left = gauss_exp_1_left * gauss_exp_2_left / p_left
            P_left = (gauss_exp_1_left*Coord_1 + gauss_exp_2_left*Coord_2) / p_left
            XPA_left = P_left - Coord_1
            XPB_left = P_left - Coord_2
            p12_left = 1.0/(2.0*p_left)
            E_buff_1 = E_1_1_2(q_left, p12_left, XAB_left, XPA_left, XPB_left, E_buff_1)
            for k in range(0, number_primitive_3):
                gauss_exp_1_right = gauss_exp_3[k]
                for l in range(0, number_primitive_4):
                    gauss_exp_2_right = gauss_exp_4[l]
                    p_right = gauss_exp_1_right + gauss_exp_2_right
                    q_right = gauss_exp_1_right * gauss_exp_2_right / p_right
                    P_right = (gauss_exp_1_right*Coord_3 + gauss_exp_2_right*Coord_4) / p_right
                    alpha = p_left*p_right/(p_left+p_right)
                    XPC, YPC, ZPC = P_left - P_right
                    RPC = ((XPC)**2+(YPC)**2+(ZPC)**2)**0.5
                    XPA_right = P_right - Coord_3
                    XPB_right = P_right - Coord_4
                    p12_right = 1.0/(2.0*p_right)
                    E_buff_2 = E_1_1_2(q_right, p12_right, XAB_right, XPA_right, XPB_right, E_buff_2)
                    R_array = R_1_1_1_1(alpha, XPC, YPC, ZPC, RPC, R_buffer)
                    counter = 0
                    for x1 in range(1, -1, -1):
                        for y1 in range(1-x1, -1, -1):
                            for z1 in range(1-x1-y1, 0-x1-y1, -1):
                                for x2 in range(1, -1, -1):
                                    for y2 in range(1-x2, -1, -1):
                                        for z2 in range(1-x2-y2, 0-x2-y2, -1):
                                            for x3 in range(1, -1, -1):
                                                for y3 in range(1-x3, -1, -1):
                                                    for z3 in range(1-x3-y3, 0-x3-y3, -1):
                                                        for x4 in range(1, -1, -1):
                                                            for y4 in range(1-x4, -1, -1):
                                                                for z4 in range(1-x4-y4, 0-x4-y4, -1):
                                                                    primitives_buffer[i,j,k,l,counter] = ERI_expansion_coeff_sum(E_buff_1[x1,x2,:,0],E_buff_1[y1,y2,:,1],E_buff_1[z1,z2,:,2],E_buff_2[x3,x4,:,0],E_buff_2[y3,y4,:,1],E_buff_2[z3,z4,:,2],R_array,x1+x2+1,y1+y2+1,z1+z2+1,x3+x4+1,y3+y4+1,z3+z4+1)
                                                                    counter += 1
                    primitives_buffer[i,j,k,l,:81] = 1.0/(p_left*p_right*(p_left+p_right)**0.5)*primitives_buffer[i,j,k,l,:81]
    for i in range(0, 81):
        output_buffer[i] = Contraction_two_electron(primitives_buffer[:,:,:,:,i], Contra_coeffs_1, Contra_coeffs_2, Contra_coeffs_3, Contra_coeffs_4)*144.43253338822566
    return output_buffer

