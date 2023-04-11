using UnityEngine;
using UnityEngine.SceneManagement;

public class Loading : MonoBehaviour
{
    public void QuitVR()
    {
        UnityEngine.XR.XRSettings.enabled = false;
        Debug.Log("Exiting VR...");
        SceneManager.LoadScene(36);
    }

    public void LoadVR()
    {
        SceneManager.LoadScene("CPR-Module");
    }
    public void BacktoStart()
    {
        SceneManager.LoadScene(0);
    }
}
