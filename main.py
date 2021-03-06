from GUI import Ui_MainWindow
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import numpy as np
import func
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *



class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionLoad_Image.triggered.connect(self.Load_img)

        self.ui.noise_comboBox.activated.connect(lambda current_text:
                                                 self.noise_choosen(self.ui.noise_comboBox.currentText(), self.Display_Original_img()))
        self.ui.filters_comboBox.activated.connect(lambda current_text:
                                                   self.filter_choosen(self.ui.filters_comboBox.currentText(),
                                                                       self.noise_choosen(self.ui.noise_comboBox.currentText(),
                                                                                          self.Display_Original_img())))
        self.ui.Edge_comboBox.activated.connect(lambda current_text:self.edge_detector(self.ui.Edge_comboBox.currentText()
                                                                                       ,self.Display_Original_img()))


        self.ui.actionHistogram.triggered.connect(self.Histogram)
        self.ui.actionRGB_Histogram.triggered.connect(self.RGB_Histogram)
        self.ui.actionHyprid_Image.triggered.connect(self.Hyprid_Image)
        self.ui.actionImage_Equalization.triggered.connect(self.img_equalization)
        self.ui.actionImage_Normalization.triggered.connect(self.img_normalization)
        self.ui.actionGlobal_Threshold.triggered.connect(self.global_Threshold)
        self.ui.actionLocal_Threshold.triggered.connect(self.local_Threshold)





    def noise_choosen(self, noise, img):


        if noise == 'Salt&pepper':
            noisy_img = func.salt_pepper_noise(img)
            self.display_noisy_img(noisy_img)
        elif noise == 'Gaussian':
            noisy_img = func.gussian_noise(img)
            self.display_noisy_img(noisy_img)
        else:
            noisy_img = func.uniform_noise(img)
            self.display_noisy_img(noisy_img)

        return noisy_img


    def filter_choosen(self, filter, noisy_img):
        if filter == 'average filter':
            ave_img = func.ave_filter(noisy_img)
            self.display_filtered_img(ave_img)
        elif filter == 'Gaussian filter':
            gauss_img = func.gaussian_filter(noisy_img, (9, 9))
            self.display_filtered_img(gauss_img)
        elif filter == 'Median filter':
            median_img = func.median_filter(noisy_img)
            self.display_filtered_img(median_img)
        elif filter == 'Freq. low pass filter':
            freq_LPF = func.freq_domain_filter(noisy_img, 'lpf')
            self.display_filtered_img(freq_LPF)
        else:
            freq_HPF = func.freq_domain_filter(noisy_img, 'hpf')
            self.display_filtered_img(freq_HPF)



    def edge_detector(self, edge, img):
        if edge == 'Sobel Edge':
            sobel_img, _ = func.sobel_edge(img)

            self.display_filtered_img(sobel_img)

        elif edge == 'Roberts Edge':
            robert_img = func.roberts_edge(img)
            self.display_filtered_img(robert_img)

        elif edge == 'Perwitt Edge':
            perwitt_img = func.perwitt_edge(img)
            self.display_filtered_img(perwitt_img)

        else:
            cany_img = func.canny_edge(img)
            self.display_filtered_img(cany_img)


    def Histogram(self):

        filename, _ = QFileDialog.getOpenFileNames(self, "Select file(s)", " ", "Images (*.png *.xpm *.jpg)")
        if len(filename) == 1 and filename != []:
            self.ui.label_8.setText("             HISTOGRAM")
            self.ui.label_6.setText("             HISTOGRAM")
            self.ui.label_9.setText("             HISTOGRAM")

            image= self.Display_img(False, filename, False)
            cv2.imwrite("result_gray.jpg", image)
            gry_result = QPixmap("result_gray.jpg").scaled(500, 500)
            self.ui.ip_img.setPixmap(QPixmap(gry_result))

            func.histogram(image, " ")

            histogram = QPixmap("Histogram.png").scaled(500, 500)
            self.ui.ip_img_2.setPixmap(QPixmap(histogram))

    def RGB_Histogram(self):

        filename, _ = QFileDialog.getOpenFileNames(self, "Select file(s)", " ", "Images (*.png *.xpm *.jpg)")
        if len(filename) == 1 and filename != []:
            self.ui.label_8.setText("             R-HISTOGRAM")
            self.ui.label_6.setText("             G-HISTOGRAM")
            self.ui.label_9.setText("             B-HISTOGRAM")

            image = self.Display_img(False,filename, True)
            cv2.imwrite("result_gray.jpg", image)
            gry_result = QPixmap("result_gray.jpg").scaled(500, 500)
            self.ui.ip_img.setPixmap(QPixmap(gry_result))

            func.rgb_histo(image, 'red')
            func.rgb_histo(image, 'green')
            func.rgb_histo(image, 'blue')

            RED_hsito = QPixmap("red_Histogram.png").scaled(500, 500)
            GREEN_histo = QPixmap("green_Histogram.png").scaled(500, 500)
            BLUE_histo = QPixmap("blue_Histogram.png").scaled(500, 500)

            self.ui.ip_img_2.setPixmap(QPixmap(RED_hsito))
            self.ui.ip_img_3.setPixmap(QPixmap(GREEN_histo))
            self.ui.ip_img_4.setPixmap(QPixmap(BLUE_histo))



    def Hyprid_Image(self):
        filename, _ = QFileDialog.getOpenFileNames(self, "Select file(s)", " ", "Images (*.png *.xpm *.jpg)")
        if len(filename) == 2 and filename != []:
            image1, image2 = self.Display_img(True, filename, False)

            cv2.imwrite("result_gray1.jpg", image1)
            gry_result1 = QPixmap("result_gray1.jpg").scaled(500, 500)
            self.ui.ip_hyp_img1.setPixmap(QPixmap(gry_result1))

            cv2.imwrite("result_gray2.jpg", image2)
            gry_result2 = QPixmap("result_gray2.jpg").scaled(500, 500)
            self.ui.ip_hyp_img2.setPixmap(QPixmap(gry_result2))

            Hyprid_img = func.hybrid(image1,image2)

            cv2.imwrite("hyprid.jpg", Hyprid_img)
            Hyprid_img_saved = QPixmap("hyprid.jpg").scaled(500, 500)
            self.ui.op_hyp_img.setPixmap(QPixmap(Hyprid_img_saved))

    def img_equalization(self):
        filename, _ = QFileDialog.getOpenFileNames(self, "Select file(s)", " ", "Images (*.png *.xpm *.jpg)")
        if len(filename) == 1 and filename != []:
            image = self.Display_img(False, filename, False)

            cv2.imwrite("result_gray.jpg", image)
            gry_result = QPixmap("result_gray.jpg").scaled(500, 500)
            self.ui.ip_img_eq.setPixmap(QPixmap(gry_result))

            eq_img = func.equalize_image(image)

            cv2.imwrite("Eq_img.jpg", eq_img)
            Eq_img = QPixmap("Eq_img.jpg").scaled(500, 500)
            self.ui.op_img_eq.setPixmap(QPixmap(Eq_img))

    def img_normalization(self):
        filename, _ = QFileDialog.getOpenFileNames(self, "Select file(s)", " ", "Images (*.png *.xpm *.jpg)")
        if len(filename) == 1 and filename != []:
            self.ui.label_14.setText('           Normalized IMAGE')

            image = self.Display_img(False, filename, False)

            cv2.imwrite("result_gray.jpg", image)
            gry_result = QPixmap("result_gray.jpg").scaled(500, 500)
            self.ui.ip_img_eq.setPixmap(QPixmap(gry_result))

            norm_img = func.normalize(image, True)

            cv2.imwrite("Norm_img.jpg", norm_img)
            Norm_img = QPixmap("Norm_img.jpg").scaled(500, 500)

            self.ui.op_img_eq.setPixmap(QPixmap(Norm_img))

    def global_Threshold(self):
        filename, _ = QFileDialog.getOpenFileNames(self, "Select file(s)", " ", "Images (*.png *.xpm *.jpg)")
        if len(filename) == 1 and filename != []:
            self.ui.label_14.setText('           Global Threshold')

            image = self.Display_img(False, filename, False)

            cv2.imwrite("result_gray.jpg", image)
            gry_result = QPixmap("result_gray.jpg").scaled(500, 500)
            self.ui.ip_img_eq.setPixmap(QPixmap(gry_result))

            Global_th = func.global_Thresholding(image)

            cv2.imwrite("Norm_img.jpg", Global_th)
            Globla_img = QPixmap("Norm_img.jpg").scaled(500, 500)

            self.ui.op_img_eq.setPixmap(QPixmap(Globla_img))

    def local_Threshold(self):
        filename, _ = QFileDialog.getOpenFileNames(self, "Select file(s)", " ", "Images (*.png *.xpm *.jpg)")
        if len(filename) == 1 and filename != []:
            self.ui.label_14.setText('           Local Threshold')

            image = self.Display_img(False, filename, False)

            cv2.imwrite("result_gray.jpg", image)
            gry_result = QPixmap("result_gray.jpg").scaled(500, 500)
            self.ui.ip_img_eq.setPixmap(QPixmap(gry_result))

            Local_th = func.local_Thresholding(image)

            cv2.imwrite("Norm_img.jpg", Local_th)
            Local_img = QPixmap("Norm_img.jpg").scaled(500, 500)

            self.ui.op_img_eq.setPixmap(QPixmap(Local_img))



    # helper functiions
    def Display_img(self, Multi_Images, filename, RGB):
        if Multi_Images:
            img1 = cv2.imread(f'{filename[0]}')
            img2 = cv2.imread(f'{filename[1]}')
            gray_img1 = np.dot(img1[..., :3], [0.2989, 0.5870, 0.1140])
            gray_img2 = np.dot(img2[..., :3], [0.2989, 0.5870, 0.1140])

            return gray_img1, gray_img2

        elif RGB:
            return cv2.imread(f'{filename[0]}')
        else:
            img = cv2.imread(f'{filename[0]}')
            gray_img = np.dot(img[..., :3], [0.2989, 0.5870, 0.1140])

            return gray_img


    def display_noisy_img(self,img):
        cv2.imwrite("result.jpg", img)
        noisy_img = QPixmap("result.jpg").scaled(500, 500)
        self.ui.noisy_image.setPixmap(QPixmap(noisy_img))


    def display_filtered_img(self,img):
        cv2.imwrite("result.jpg", img)
        filtered_img = QPixmap("result.jpg").scaled(500, 500)
        self.ui.filtered_image.setPixmap(QPixmap(filtered_img))

    def Load_img(self):
        filename, _ = QFileDialog.getOpenFileNames(self, "Select file(s)", " ", "Images (*.png *.xpm *.jpg)")
        self.img = cv2.imread(f'{filename[0]}')
        self.Display_Original_img()

    def Display_Original_img(self):
        # filename, _ = QFileDialog.getOpenFileNames(self, "Select file(s)", " ", "Images (*.png *.xpm *.jpg)")

        # img = cv2.imread(f'{filename[0]}')
        gray_img = np.dot(self.img[..., :3], [0.2989, 0.5870, 0.1140])
        cv2.imwrite("result_gray.jpg", gray_img)
        gry_result = QPixmap("result_gray.jpg").scaled(500, 500)

        self.ui.original_image.setPixmap(QPixmap(gry_result))

        return  gray_img

def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()

if __name__ == "__main__":
    main()

