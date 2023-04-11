using UnityEngine;
using UnityEngine.SceneManagement;

public class Loading : MonoBehaviour
{
    public void QuitVR()
    {
        UnityEngine.XR.XRSettings.enabled = false;
        SceneManager.LoadScene("PostAssesment/PostAssesment");
    }

    public void LoadVR()
    {
        SceneManager.LoadScene("CPR-Module");
    }

}
