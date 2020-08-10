import os
from PyPDF2 import PdfFileReader, PdfFileWriter



for index in range(1, 4): #总共有4个文件夹
		pdfFiles = []
		for root, dirs, files in os.walk('./photo/%s'%(index)):
			for file in files:
				if file.endswith('.pdf'):
					pdfFiles.append(os.path.join(root,file))

		pdfFiles.sort()


		OutputContainer = PdfFileWriter()

		for file in pdfFiles:
			inputPdf = PdfFileReader(open(file,'rb')) 
			num = inputPdf.getNumPages()
			for i in range(num):
				OutputContainer.addPage(inputPdf.getPage(i))
		os.mkdir('./res/res%s'%(index))
		OutputContainer.write(open('./res/res%s/res%s.pdf'%(index,index),'wb')) #输出也按照文件的序号完成命名
