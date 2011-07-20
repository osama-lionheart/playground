Augmented Reality cross platform plugin for unity
=================================================

Installation
------------

 - The main repo can be found at "//Osama-PC/repos/swg_ar"
 - Place this repo under your "Assets/src/" folder.
 - Move the "Plugins" and "Resources" folders inside your "Assets" folder.
 - Move the "opencv_core220.dll" and "opencv_highgui220.dll" to the root of your unity project, when you build to Windows make sure that these dlls are beside the executable file.

Usage Scenario
--------------

There are two scenarios to use this library:

 1. Through the provided behaviours in "AR/Behaviours":
 
     - To enable the tracking add "AR/Behaviours/ARTrackerBehaviour.cs" component on your main camera.
     - To add markers, use any of the following methods.
     - Add "AR/Behaviours/ARMarkerBehaviour.cs" component to any GameObject and the game object position and rotation will be updated by the tracker.
     - Get a reference to SWG.AR.Behaviours.ARMarkerBehaviour.manager and use its API to Add/Remove markers , note that you can only Add/Remove markers with this usage scenario since the manager will be initialized in the behaviour automatically.
	 
 2. Through the SWG.AR.ARManager class that provide a singleton API to accees all the functionalities provided with this plugin, for sample code refer to "AR/Behaviours/ARTrackerBehaviour.cs".