#include <baseapi.h>
#include <allheaders.h>

int main() {
    tesseract::TessBaseAPI *myOCR = new tesseract::TessBaseAPI();
    if (myOCR->Init(NULL, "eng")) {
        fprintf(stderr, "Could not initialize tesseract.\n");
        exit(1);
    }
    Pix *pix = pixRead("in.jpeg");
    myOCR->SetImage(pix);
    char* outText = myOCR->GetUTF8Text();
    printf("OCR output:\n\n");
    printf(outText);

    myOCR->Clear();
    myOCR->End();
    delete[] outText;
    pixDestroy(&pix);
    return 0;
}
