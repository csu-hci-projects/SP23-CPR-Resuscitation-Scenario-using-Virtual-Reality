using UnityEngine;
using UnityEngine.UI;
using UnityEngine.Video;

public class PlayButton : MonoBehaviour
{
    public VideoPlayer videoPlayer;
    private bool videoWasPlayed = false;
    public GameObject button;

    public void PlayVideo()
    {
        videoPlayer.Play();
    }

    void Update()
    {
        if (videoPlayer.isPlaying && !videoWasPlayed)
        {
            videoWasPlayed = true;
        }
        else if (!videoPlayer.isPlaying && videoWasPlayed)
        {
            button.SetActive(true);
        }
    }
}