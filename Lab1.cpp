#define WIN32_LEAN_AND_MEAN
#include <windows.h>
#include "module1.h"
#include "module2.h"
#include "module3.h"

enum { IDM_WORK1 = 1, IDM_WORK2 };

static const wchar_t CLASS_NAME[] = L"Lab1Window";
static const wchar_t WND_TITLE[]  = L"Lab1";

static wchar_t g_szResult[256] = L"";

static LRESULT CALLBACK WndProc(HWND, UINT, WPARAM, LPARAM);
static void Work1(HWND hWnd);
static void Work2(HWND hWnd);
static HMENU CreateAppMenu();

int WINAPI wWinMain(HINSTANCE hInstance, HINSTANCE, LPWSTR, int nCmdShow)
{
    WNDCLASSEXW wc = {};
    wc.cbSize        = sizeof(wc);
    wc.style         = CS_HREDRAW | CS_VREDRAW;
    wc.lpfnWndProc   = WndProc;
    wc.hInstance     = hInstance;
    wc.hIcon         = LoadIcon(nullptr, IDI_APPLICATION);
    wc.hCursor       = LoadCursor(nullptr, IDC_ARROW);
    wc.hbrBackground = (HBRUSH)(COLOR_WINDOW + 1);
    wc.lpszClassName = CLASS_NAME;
    wc.hIconSm       = LoadIcon(nullptr, IDI_APPLICATION);
    RegisterClassExW(&wc);

    HWND hWnd = CreateWindowW(CLASS_NAME, WND_TITLE, WS_OVERLAPPEDWINDOW,
        CW_USEDEFAULT, 0, CW_USEDEFAULT, 0, nullptr, CreateAppMenu(), hInstance, nullptr);
    if (!hWnd)
        return FALSE;

    ShowWindow(hWnd, nCmdShow);
    UpdateWindow(hWnd);

    MSG msg;
    while (GetMessage(&msg, nullptr, 0, 0))
    {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }
    return (int)msg.wParam;
}

static HMENU CreateAppMenu()
{
    HMENU hMenu = CreateMenu();
    AppendMenuW(hMenu, MF_STRING, IDM_WORK1, L"Робота&1");
    AppendMenuW(hMenu, MF_STRING, IDM_WORK2, L"Робота&2");
    return hMenu;
}

static LRESULT CALLBACK WndProc(HWND hWnd, UINT message, WPARAM wParam, LPARAM lParam)
{
    switch (message)
    {
    case WM_COMMAND:
        switch (LOWORD(wParam))
        {
        case IDM_WORK1:
            Work1(hWnd);
            break;
        case IDM_WORK2:
            Work2(hWnd);
            break;
        }
        break;

    case WM_PAINT:
    {
        PAINTSTRUCT ps;
        HDC hdc = BeginPaint(hWnd, &ps);
        if (g_szResult[0] != 0)
            TextOutW(hdc, 20, 20, g_szResult, lstrlenW(g_szResult));
        EndPaint(hWnd, &ps);
        break;
    }

    case WM_DESTROY:
        PostQuitMessage(0);
        break;

    default:
        return DefWindowProc(hWnd, message, wParam, lParam);
    }
    return 0;
}

static void Work1(HWND hWnd)
{
    int value = 50;

    if (Func_MOD1(hWnd, &value) != 0)
    {
        wsprintfW(g_szResult, L"Вибране число: %d", value);
        InvalidateRect(hWnd, nullptr, TRUE);
    }
}

static void Work2(HWND hWnd)
{
    int step = 1;

    for (;;)
    {
        if (step == 1)
        {
            if (Func_MOD2(hWnd) == 1)
                step = 2;
            else
                break;
        }
        else
        {
            int r = Func_MOD3(hWnd);
            if (r == -1)
            {
                step = 1;
            }
            else
            {
                if (r == 1)
                {
                    lstrcpyW(g_szResult, L"Робота2: у другому вікні натиснуто [Так]");
                    InvalidateRect(hWnd, nullptr, TRUE);
                }
                break;
            }
        }
    }
}
