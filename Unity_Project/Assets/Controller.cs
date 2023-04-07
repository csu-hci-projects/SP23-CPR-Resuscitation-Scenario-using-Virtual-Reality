using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class EndMenu : MonoBehaviour
{
    public static bool GamePaused = false;

    public GameObject pausedUI;
    public GameObject failedUI;
    public GameObject winUI;
    public static EndMenu instance;
    public GameObject speedText;
    public GameObject heightText;
    public GameObject throttleText;
    public GameObject cross;
    public GameObject circle;
    public Camera cam;

    private void Awake()
    {
        if (instance == null)
        {
            instance = this;
            Resume();
        }
    }
    private void Start()
    {
        pausedUI.SetActive(false);
        failedUI.SetActive(false);
        winUI.SetActive(false);

    }
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Escape))
        {
            if (GamePaused)
            {
                Resume();
            }
            else
            {
                Paused();
            }
        }
    }

    public void Resume()
    {
        pausedUI.SetActive(false);
        Time.timeScale = 1f;

        speedText.SetActive(true);
        heightText.SetActive(true);
        throttleText.SetActive(true);
        cross.SetActive(true);
        circle.SetActive(true);

        GamePaused = false;
        Debug.Log($"Resuming Game...");
    }

    void Paused()
    {
        pausedUI.SetActive(true);
        Time.timeScale = 0f;
        GamePaused = true;

        speedText.SetActive(false);
        heightText.SetActive(false);
        throttleText.SetActive(false);
        cross.SetActive(false);
        circle.SetActive(false);
        stopCam();

        Debug.Log($"Pausing Game...");
    }

    public void Restart()
    {
        Debug.Log($"Restarting Game...");

        speedText.SetActive(true);
        heightText.SetActive(true);
        throttleText.SetActive(true);
        cross.SetActive(true);
        circle.SetActive(true);

        SceneManager.LoadScene(SceneManager.GetActiveScene().name);
        Resume();
    }

    public void Exit()
    {
        Debug.Log($"Exiting Game...");
        Application.Quit();
    }

    void stopCam()
    {
        cam.transform.position = new Vector3(cam.transform.position.x, cam.transform.position.y, cam.transform.position.z);
    }
}
