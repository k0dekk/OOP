#include "module3.h"
#include "resource.h"

static INT_PTR CALLBACK DlgProc_MOD3(HWND, UINT, WPARAM, LPARAM);

int Func_MOD3(HWND hWnd)
{
    INT_PTR res = DialogBox((HINSTANCE)GetWindowLongPtr(hWnd, GWLP_HINSTANCE),
                            MAKEINTRESOURCE(IDD_DIALOG_MOD3),
                            hWnd,
                            DlgProc_MOD3);

    if (res == 1 || res == -1)
        return (int)res;
    return 0;
}

INT_PTR CALLBACK DlgProc_MOD3(HWND hDlg, UINT message, WPARAM wParam, LPARAM lParam)
{
    UNREFERENCED_PARAMETER(lParam);

    switch (message)
    {
    case WM_INITDIALOG:
        return (INT_PTR)TRUE;

    case WM_COMMAND:
        switch (LOWORD(wParam))
        {
        case IDC_BACK_MOD3:
            EndDialog(hDlg, -1);
            return (INT_PTR)TRUE;
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
