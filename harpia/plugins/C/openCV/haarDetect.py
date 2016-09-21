#!/usr/bin/env python
 # -*- coding: utf-8 -*-

from harpia.constants import *
import gettext
_ = gettext.gettext
gettext.bindtextdomain(APP, DIR)
gettext.textdomain(APP)

from harpia.GUI.fieldtypes import *
from harpia.plugins.C.openCV.opencvplugin import OpenCVPlugin

class HaarDetect(OpenCVPlugin):

# ------------------------------------------------------------------------------
    def __init__(self):
        OpenCVPlugin.__init__(self)
        self.id = -1
        self.type = self.__class__.__module__
        self.cascade_name ="/usr/share/harpia/images/haarcascade_frontalface_alt2.xml"
        self.min_neighbors = 2

    # ----------------------------------------------------------------------
    def get_help(self):
        return "Detecta formas circulares na imagem de entrada. Saida 1 é a resposta da avaliacao(*) e a saida dois mostra os circulos encontrados."

    # ----------------------------------------------------------------------
    def generate_vars(self):
        return \
            'IplImage * block$id$_img_i1 = NULL;\n' + \
            'CvPoint block$id$_point_o1 = cvPoint(0,0);\n' + \
            'CvRect block$id$_rect_o2 = cvRect( 0, 0, 1, 1);\n' + \
            'IplImage * block$id$_img_o3 = NULL;\n' + \
            'double block$id$_double_o4 = 0.0;\n' + \
            'static CvMemStorage* block$id$_storage = 0;\n' + \
            'static CvHaarClassifierCascade* block$id$_cascade = 0;\n' + \
            'const char* block$id$_cascade_name = "$cascade_name$";\n'

    # ----------------------------------------------------------------------
    def generate_function_call(self):
        return \
             '\nif(block$id$_img_i1){\n' + \
             '	double scale = 1.3;\n' + \
             '	block$id$_cascade = (CvHaarClassifierCascade*)cvLoad( block$id$_cascade_name, 0, 0, 0 );\n' + \
             '	IplImage* gray = cvCreateImage( cvSize(block$id$_img_i1->width,block$id$_img_i1->height), 8, 1 );\n' + \
             '	IplImage* small_img = cvCreateImage( cvSize( cvRound (block$id$_img_i1->width/scale), cvRound (block$id$_img_i1->height/scale)),8, 1 );\n' + \
             '	cvCvtColor( block$id$_img_i1, gray, CV_BGR2GRAY );\n' + \
             '	cvResize( gray, small_img, CV_INTER_LINEAR );\n' + \
             '	cvEqualizeHist( small_img, small_img );\n' + \
             '	if(!block$id$_img_o3)\n' + \
             '	block$id$_img_o3 = cvCloneImage(block$id$_img_i1);\n' + \
             '	cvCopy(block$id$_img_i1,block$id$_img_o3,0);\n' + \
             '	block$id$_storage = cvCreateMemStorage(0);\n' + \
             '	cvClearMemStorage( block$id$_storage );\n' + \
             '	block$id$_rect_o2 = cvRect( 0, 0, 1, 1);\n' + \
             '	CvSeq* faces = cvHaarDetectObjects(small_img, ' + \
             'block$id$_cascade, block$id$_storage,1.1, $min_neighbors$, 0/*CV_HAAR_DO_CANNY_PRUNING*/,cvSize(30, 30) );\n' + \
             '	block$id$_double_o4 = faces->total;\n' + \
             '	if(faces)\n' + \
             '	{\n' + \
             '		int i;\n' + \
             '		for( i = 0; i < (faces ? faces->total : 0); i++ )\n' + \
             '		{\n' + \
             '		CvRect* r = (CvRect*)cvGetSeqElem( faces, i );\n' + \
             '			if(r)\n' + \
             '			{\n' + \
             '				CvPoint center;\n' + \
             '				int radius;\n' + \
             '				center.x = cvRound((r->x + r->width*0.5)*scale);\n' + \
             '				center.y = cvRound((r->y + r->height*0.5)*scale);\n' + \
             '				radius = cvRound((r->width + r->height)*0.25*scale);\n' + \
             '				cvCircle( block$id$_img_o3, center, radius, cvScalarAll(0), 3, 8, 0 );\n' + \
             '				if(i == 0)\n' + \
             '				{\n' + \
             '					block$id$_point_o1 = center;\n' + \
             '					block$id$_rect_o2.x = (r->x)*scale;\n' + \
             '					block$id$_rect_o2.y = (r->y)*scale;\n' + \
             '					block$id$_rect_o2.width = (r->width)*scale;\n' + \
             '					block$id$_rect_o2.height = (r->height)*scale;\n' + \
             '				}\n' + \
             '			}\n' + \
             '		}\n' + \
             '	}\n' + \
             '	cvReleaseImage( &gray );\n' + \
             '	cvReleaseImage( &small_img );\n' + \
             '}\n'

    # ----------------------------------------------------------------------
    def generate_dealloc(self):
        return 'cvReleaseImage(&block$id$_img_o3);\n' + \
               'cvReleaseImage(&block$id$_img_i1);\n' + \
               'cvReleaseMemStorage(&block$id$_storage);\n'

    # ----------------------------------------------------------------------
    def __del__(self):
        pass

    # ----------------------------------------------------------------------
    def get_description(self):
        return {"Type": str(self.type),
                'Label': _('Haar (face) Detector'),
                'Icon': 'images/haarDetect.png',
                'Color': '50:220:40:150',
                'InTypes': {0: 'HRP_IMAGE'},
                'OutTypes': {0: 'HRP_POINT', 1: 'HRP_RECT', 2: 'HRP_IMAGE', 3: 'HRP_DOUBLE'},
                'Description': _('Haar (face) Detector finds regions on the input image according to the given haar-classifier. \n First Output is the center of the first \
detected feature, second is a rectangle around the first detected feature and the third is the input image with the detected features tagged by a red circle.\n \
The last output is the number of detected faces.'),
                'TreeGroup': _("Feature Detection")
            }

    # ----------------------------------------------------------------------
    def get_properties(self):
        return {

                    "cascade_name":{"name": "File Name",
                            "type": HARPIA_SAVE_FILE,
                            "value": self.cascade_name},

                "min_neighbors":{"name": "Min neighbors",
                    "type": HARPIA_INT,
                    "value": self.min_neighbors,
                    "lower":1,
                    "upper":99,
                    "step":1
                    },

        }

# ------------------------------------------------------------------------------
