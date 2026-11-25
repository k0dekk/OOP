#include "module1.h"
#include "resource.h"

#define SCROLL_MIN_MOD1     1
#define SCROLL_MAX_MOD1     100
#define SCROLL_PAGE_MOD1    10

static int *s_pValue = nullptr;

static INT_PTR CALLBACK DlgProc_MOD1(HWND, UINT, WPARAM, LPARAM);
static BOOL onInit_MOD1(HWND hDlg);
static void onHScroll_MOD1(HWND hDlg, WPARAM wParam, LPARAM lParam);
static void onClickOk_MOD1(HWND hDlg);
static int  Clamp_MOD1(int pos);

int Func_MOD1(HWND hWnd, int *pValue)
{
    s_pValue = pValue;

    INT_PTR res = DialogBox((HINSTANCE)GetWindowLongPtr(hWnd, GWLP_HINSTANCE),
                            MAKEINTRESOURCE(IDD_DIALOG_MOD1),
                            hWnd,
                            DlgProc_MOD1);

    return (res == 1) ? 1 : 0;
}

INT_PTR CALLBACK DlgProc_MOD1(HWND hDlg, UINT message, WPARAM wParam, LPARAM lParam)
{
    switch (message)
    {
    case WM_INITDIALOG:
        return onInit_MOD1(hDlg);

    case WM_HSCROLL:
        onHScroll_MOD1(hDlg, wParam, lParam);
        return (INT_PTR)TRUE;

    case WM_COMMAND:
        switch (LOWORD(wParam))
        {
        case IDOK:
            onClickOk_MOD1(hDlg);
            return (INT_PTR)TRUE;
        case IDCANCEL:
            EndDialog(hDlg, 0);
            return (INT_PTR)TRUE;
        }
        break;
    }
    return (INT_PTR)FALSE;
}

static int Clamp_MOD1(int pos)
{
    if (pos < SCROLL_MIN_MOD1) return SCROLL_MIN_MOD1;
    if (pos > SCROLL_MAX_MOD1) return SCROLL_MAX_MOD1;
    return pos;
}

static BOOL onInit_MOD1(HWND hDlg)
{
    HWND hScroll = GetDlgItem(hDlg, IDC_SCROLLBAR_MOD1);

    SetScrollRange(hScroll, SB_CTL, SCROLL_MIN_MOD1, SCROLL_MAX_MOD1, FALSE);

    int pos = Clamp_MOD1(s_pValue ? *s_pValue : SCROLL_MIN_MOD1);
    SetScrollPos(hScroll, SB_CTL, pos, TRUE);
    SetDlgItemInt(hDlg, IDC_VALUE_MOD1, pos, FALSE);

    return TRUE;
}

static void onHScroll_MOD1(HWND hDlg, WPARAM wParam, LPARAM lParam)
{
    HWND hScroll = (HWND)lParam;
    if (hScroll != GetDlgItem(hDlg, IDC_SCROLLBAR_MOD1))
        return;

    int pos = GetScrollPos(hScroll, SB_CTL);

    switch (LOWORD(wParam))
    {
    case SB_LINELEFT:   pos--;                        break;
    case SB_LINERIGHT:  pos++;                        break;
    case SB_PAGELEFT:   pos -= SCROLL_PAGE_MOD1;      break;
    case SB_PAGERIGHT:  pos += SCROLL_PAGE_MOD1;      break;
    case SB_LEFT:       pos = SCROLL_MIN_MOD1;        break;
    case SB_RIGHT:      pos = SCROLL_MAX_MOD1;        break;
    case SB_THUMBTRACK:
    case SB_THUMBPOSITION:
        pos = HIWORD(wParam);
        break;
    default:
        return;
    }

    pos = Clamp_MOD1(pos);
    SetScrollPos(hScroll, SB_CTL, pos, TRUE);
    SetDlgItemInt(hDlg, IDC_VALUE_MOD1, pos, FALSE);
}

static void onClickOk_MOD1(HWND hDlg)
{
    if (s_pValue)
        *s_pValue = GetScrollPos(GetDlgItem(hDlg, IDC_SCROLLBAR_MOD1), SB_CTL);

    EndDialog(hDlg, 1);
}
