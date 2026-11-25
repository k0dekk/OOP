#include "module2.h"
#include "resource.h"

static INT_PTR CALLBACK DlgProc_MOD2(HWND, UINT, WPARAM, LPARAM);

int Func_MOD2(HWND hWnd)
{
    INT_PTR res = DialogBox((HINSTANCE)GetWindowLongPtr(hWnd, GWLP_HINSTANCE),
                            MAKEINTRESOURCE(IDD_DIALOG_MOD2),
                            hWnd,
                            DlgProc_MOD2);

    return (res == 1) ? 1 : 0;
}

INT_PTR CALLBACK DlgProc_MOD2(HWND hDlg, UINT message, WPARAM wParam, LPARAM lParam)
{
    UNREFERENCED_PARAMETER(lParam);

    switch (message)
    {
    case WM_INITDIALOG:
        return (INT_PTR)TRUE;

    case WM_COMMAND:
        switch (LOWORD(wParam))
        {
        case IDOK:
            EndDialog(hDlg, 1);
            return (INT_PTR)TRUE;
        case IDCANCEL:
            EndDialog(hDlg, 0);
            return (INT_PTR)TRUE;
        }
        break;
    }
    return (INT_PTR)FALSE;
}
